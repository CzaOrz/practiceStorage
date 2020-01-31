DESC = 0
ASC = 1


def filling(func):
    def wrapper(self, *args, **kwargs):
        if self.length <= 1:
            return self.queue
        self.queue[:] = self.source
        func(self, *args, **kwargs)
        return self.queue

    return wrapper


class SortingAlgorithm:

    def __init__(self, queue: list):
        self.source = queue
        self.queue = []
        self.length = len(queue)
        self._count = 0

    @property
    def count(self):
        count = self._count
        self._count = 0
        return count

    def _exchange(self, i, j):
        self._count += 1
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

    @filling
    def bubble_sort(self, sort=ASC):
        flag = False
        for i in range(self.length - 1):
            for j in range(self.length - i - 1):
                if sort == ASC and self.queue[j] > self.queue[j + 1]:
                    flag = True
                    self._exchange(j, j + 1)
                elif sort == DESC and self.queue[j] < self.queue[j + 1]:
                    flag = True
                    self._exchange(j, j + 1)
            if flag is False:
                break
            flag = False

    @filling
    def select_sort(self, sort=ASC):
        for i in range(self.length - 1):
            cur_idx = aim_idx = i
            aim_value = self.queue[i]
            for j in range(i + 1, self.length):
                if sort == ASC and self.queue[j] < aim_value:
                    aim_value = self.queue[j]
                    aim_idx = j
                elif sort == DESC and self.queue[j] > aim_value:
                    aim_value = self.queue[j]
                    aim_idx = j
            if cur_idx != aim_idx:
                self._exchange(cur_idx, aim_idx)

    @filling
    def insert_sort(self, sort=ASC):
        for i in range(1, self.length):
            while i >= 1:
                if sort == ASC and self.queue[i] < self.queue[i - 1]:
                    pass
                elif sort == DESC and self.queue[i] > self.queue[i - 1]:
                    pass
                else:
                    break
                self._exchange(i - 1, i)
                i -= 1

    @filling
    def shell_sort(self, sort=ASC):
        step = self.length // 2
        while step:
            for i in range(step, self.length):
                while i >= step:
                    if sort == ASC and self.queue[i] < self.queue[i - step]:
                        pass
                    elif sort == DESC and self.queue[i] > self.queue[i - step]:
                        pass
                    else:
                        break
                    self._exchange(i - step, i)
                    i -= step
            step //= 2



if __name__ == '__main__':
    import random

    # test1 = [random.randint(1, 100) for _ in range(10)]
    test1 = [i for i in range(1, 11)][::-1]
    test = SortingAlgorithm(test1)
    print(test1)
    # print(test.bubble_sort(), test.count)
    # print(test.bubble_sort(DESC), test.count)
    # print(test.select_sort(), test.count)
    # print(test.select_sort(DESC), test.count)
    # print(test.insert_sort(), test.count)
    # print(test.insert_sort(DESC), test.count)
    print(test.shell_sort(), test.count)
    # print(test.shell_sort(DESC), test.count)
