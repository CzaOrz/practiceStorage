from collections import deque


class MiniQueue:
    """
    Queue is a data-struct of FIFO.
    First In, First Out
    """

    def __init__(self):
        self._queue = deque()

    def push(self, data):
        self._queue.append(data)

    def pop(self):
        return self._queue.popleft()


class MiniStack:

    def __init__(self):
        self._queue = deque()

    def push(self, data):
        self._queue.append(data)

    def pop(self):
        return self._queue.pop()
