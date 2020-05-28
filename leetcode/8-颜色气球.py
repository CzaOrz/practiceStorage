# coding: utf-8
import random

from collections import Counter
from typing import Union

"""
Author: 陈子昂
Tel: 15607173521
Environ: Python >= 3.6
Subject:
    小明有一些气球想挂在墙上装饰，他希望相同颜色的气球不要挂在一起，
    写一个算法帮他得出一种可行的挂气球方式，自行定义函数，输入和返回，
    如果无法做到相同颜色的气球不挂在一起，请定义合适的异常方式返回
Theory:
    颜色最多的气球n个，其他气球总数大于n-1
"""


def yield_most_common(counter):
    counter_dict = dict(counter)
    most_item = max(counter_dict, key=counter_dict.get)
    most_items = [most_item for _ in range(counter_dict.pop(most_item))]
    while counter_dict:
        if most_items:
            yield most_items.pop()
        most_item = max(counter_dict, key=counter_dict.get)
        yield most_item
        counter_dict[most_item] -= 1
        if counter_dict[most_item] == 0:
            counter_dict.pop(most_item)


class Ball:
    def __init__(self, color=None):
        if color:
            self.color = str(color)
        else:
            self.refresh()

    def refresh(self):
        self.color = self.newColor()

    def newColor(self):
        return f'rgb({random.randrange(0, 256)}, {random.randrange(0, 256)}, {random.randrange(0, 256)})'

    @staticmethod
    def getColorFromBalls(balls):
        return [ball.color for ball in balls]

    def __str__(self):
        return f'color:{self.color}'

    __repr__ = __str__


class Answer:

    @classmethod
    def generateBall(cls, colors):
        if isinstance(colors, int):
            colors = (None for _ in range(colors))
        return [Ball(color) for color in colors]

    @classmethod
    def process_length_0(cls, counter, balls, most_common):
        return {
            'status': 1,
            'msg': '没有气球哦',
            'data': []
        }

    @classmethod
    def process_length_1(cls, counter, balls, most_common):
        if most_common[0][1] != 1:
            return {
                'status': 0,
                'msg': '只有一种颜色的气球，而且数据超过了1，无法排序哦',
                'data': []
            }
        else:
            return {
                'status': 1,
                'msg': '只有一种颜色的气球，而且仅有1个，直接排序哦',
                'data': Ball.getColorFromBalls(balls)
            }

    @classmethod
    def process_length_more(cls, counter, balls, most_common):
        first_count = most_common[0][1]
        other_count = 0
        for common in most_common[1:]:
            other_count += common[1]
        if first_count - 1 < other_count:
            return {
                'status': 1,
                'msg': '成功排序',
                'data': list(yield_most_common(counter))
            }
        else:
            return {
                'status': 0,
                'msg': '无法排序哦',
                'data': []
            }

    @classmethod
    def answer(self, n: Union[int, list] = 10):
        balls = self.generateBall(n)

        counter = Counter((ball.color for ball in balls))
        most_common = counter.most_common()
        length = most_common.__len__()
        if length == 0:
            return self.process_length_0(counter, balls, most_common)
        elif length == 1:
            return self.process_length_1(counter, balls, most_common)
        else:
            return self.process_length_more(counter, balls, most_common)


if __name__ == '__main__':
    # 测试
    print(Answer.answer([]))
    print(Answer.answer([1]))
    print(Answer.answer([1, 1]))
    print(Answer.answer([1, 1, 1, 1, 1, 1, 5, 7]))
    print(Answer.answer([1, 1, 1, 2, 3, 4, 5, 7]))
