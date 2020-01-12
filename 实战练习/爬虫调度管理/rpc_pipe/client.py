import time
import socket
from minitools.db.redisdb import get_redis_client
from .base import RPC
from utils.node import decode_node_task, encode_node_task, email, \
    timekiller, kill_pid, check_pid


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
                    master_command = sch_node.recv(1024).decode()
                    if "_" in master_command:  # kill node process
                        pid, node = master_command.split("_", 1)
                        print(f"kill {kill_pid(pid)} success")
                        get_redis_client().hdel(ConsumerConfig.redis_node_pool_tasks, node)
                    elif "DirtyProcessClear" == master_command:
                        all_node_info = get_redis_client().hgetall(ConsumerConfig.redis_node_pool_tasks)
                        dirty_process = []
                        for key, value in all_node_info.items():
                            if key.decode().endswith(ConsumerConfig.node_id) and \
                                    not check_pid(eval(value.decode())["pid"]):
                                dirty_process.append(key)
                        if dirty_process:
                            get_redis_client().hdel(ConsumerConfig.redis_node_pool_tasks, *dirty_process)
                except:
                    break
            sch_node.close()


class RPCCommand:

    @staticmethod
    def kill_pid():
        pass
