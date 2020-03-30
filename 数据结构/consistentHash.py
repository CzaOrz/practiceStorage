from minitools import AddressingAlgorithm
from typing import Dict


class RedisNode:
    def __init__(self, ip):
        self.ip = ip
        self.address = f"{ip}:6379"
        self.pool = {}

    def set(self, key, value):
        self.pool[key] = value

    def get(self, key):
        return self.pool.get(key)

    def __hash__(self):
        return AddressingAlgorithm.getBinary_32(self.ip)


class ConsistentHash:

    def __init__(self, ip_pool, virtual=3):
        self.ip_pool = ip_pool
        self.virtual = virtual
        self.all_nodes = {}  # type: Dict[{str:RedisNode}]
        self.nodes = set()
        for ip in ip_pool:
            self.addNode(ip)

    def hash(self, item):
        return AddressingAlgorithm.getBinary_32(item)

    def addNode(self, ip):
        node = RedisNode(ip)
        self.all_nodes[hash(node)] = node
        self.nodes.add(node)
        for index in range(self.virtual):
            new_ip = f"{ip}#{index}"
            hashCode = self.hash(new_ip)
            self.all_nodes[hashCode] = node

    def removeNode(self, ip):
        hashNode = self.hash(ip)
        self.all_nodes.pop(hashNode)
        for index in range(self.virtual):
            new_ip = f"{ip}#{index}"
            hashCode = self.hash(new_ip)
            self.all_nodes.pop(hashCode)

    def _findNode(self, key) -> RedisNode:
        hashKey = self.hash(key)
        firstNode = None
        for hashNode in sorted(self.all_nodes.keys()):
            if hashKey < hashNode:
                return self.all_nodes[hashNode]
            if not firstNode:
                firstNode = self.all_nodes[hashNode]
        return firstNode

    def set(self, key, value):
        node = self._findNode(key)
        node.set(key, value)

    def get(self, key):
        node = self._findNode(key)
        return node.get(key)


if __name__ == '__main__':
    ip_pool = [
        "192.168.0.1",
        "192.168.0.2",
        "192.168.0.3",
        "192.168.0.4",
        "192.168.0.5",
        "192.168.0.6",
    ]
    redisCluster = ConsistentHash(ip_pool, 100)
    import random

    values = set()
    for _ in range(200):
        key = str(random.randint(1, 1000))
        redisCluster.set(key, f"{key}##{key}")
        values.add(key)

    for node in redisCluster.nodes:
        print(node.address, len(node.pool))
