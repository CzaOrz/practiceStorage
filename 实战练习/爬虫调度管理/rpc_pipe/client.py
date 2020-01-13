import time
import socket
from minitools.db.redisdb import get_redis_client
from utils.node import kill_pid, check_pid
from .base import RPC


class RPCClient(RPC):

    def serving(self):
        while True:
            try:
                sch_node = socket.socket()
                sch_node.connect((self.host, self.port))
                sch_node.send(self.node_id.encode())
            except:
                time.sleep(10)
                continue
            while True:
                try:
                    master_command = sch_node.recv(1024)
                    if master_command == self.consumerConfig.CLEAR_DIRTY_NODE_PROCESS:
                        RPCCommand.clear_dirty_node_process(self)
                    elif b"_" in master_command:
                        RPCCommand.kill_pid(self, master_command.decode())
                except:
                    break
            sch_node.close()


class RPCCommand:

    @staticmethod
    def clear_dirty_node_process(client):
        all_node_info = get_redis_client().hgetall(client.redis_node_pool_tasks)
        dirty_process = []
        for key, value in all_node_info.items():
            if key.decode().endswith(client.node_id) and \
                    not check_pid(eval(value.decode())["pid"]):
                dirty_process.append(key)
        if dirty_process:
            get_redis_client().hdel(client.redis_node_pool_tasks, *dirty_process)

    @staticmethod
    def kill_pid(client, master_command):
        pid, node = master_command.split("_", 1)
        print(f"kill {kill_pid(pid)} success")
        get_redis_client().hdel(client.redis_node_pool_tasks, node)
