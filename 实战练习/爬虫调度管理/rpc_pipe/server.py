import time
import socket
import logging
import threading
from minitools.db.redisdb import get_redis_client
from .base import RPC

logger = logging.getLogger(__name__)
nodes = {}


def online_heartbeat():
    nodes_copy = nodes.copy()
    for node_id, node_socket in nodes_copy.items():
        try:
            node_socket.setblocking(False)
            node_socket.recv(1)
        except (BlockingIOError, socket.timeout):
            continue
        except ConnectionError:
            nodes.pop(node_id)


class RPCServer(RPC):

    def checking(self, abnormal_nodes: tuple):  # todo, how to back to check
        del_tasks = []
        for task in get_redis_client().hgetall(self.consumerConfig.redis_node_pool_tasks):
            if task.decode().endswith(abnormal_nodes):
                del_tasks.append(task)
        if del_tasks:
            logger.warning(f"delete {del_tasks}")
            get_redis_client().hdel(self.consumerConfig.redis_node_pool_tasks, *del_tasks)

    def loop_checking(self):
        old_nodes = set()
        while True:
            count = 0
            while True:
                cur_nodes = set(nodes.keys())
                if len(cur_nodes) < len(old_nodes):
                    self.checking(tuple(old_nodes ^ cur_nodes))
                    old_nodes = cur_nodes
                else:
                    old_nodes = cur_nodes
                time.sleep(10)
                count += 1
                if count == 6:
                    break
            online_heartbeat()

    def serving(self):
        sch_host = socket.socket()
        sch_host.bind(("0.0.0.0", self.port))
        sch_host.listen(3)
        while True:
            try:
                soc, host = sch_host.accept()
                node_id = soc.recv(1024).decode()
                nodes[node_id] = soc
            except:
                pass

    def run(self):
        super(RPCServer, self).run()
        thread = threading.Thread(target=self.loop_checking)
        thread.setDaemon(True)
        thread.start()
