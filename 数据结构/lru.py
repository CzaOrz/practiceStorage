from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = {}
        self.cache_list = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache_dict:
            self.cache_list.remove(key)
            self.cache_list.appendleft(key)
            return self.cache_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            self.cache_list.remove(key)
        elif len(self.cache_list) >= self.capacity:
            self.cache_dict.pop(self.cache_list.pop())
        self.cache_dict[key] = value
        self.cache_list.appendleft(key)
