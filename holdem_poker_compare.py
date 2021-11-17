# 德州扑克牌型大小比较（德州扑克不区分花色）
from enum import Enum
from typing import List

# （0 高牌）（1 对子）（2 两对）（3 三条）（4 顺子）（5 同花）（6 葫芦）（7 四条）（8 同花顺）
class Level(Enum):
    NO_PAIR = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_KIND = 7
    STRAIGHT_FLUSH = 8

# 黑桃，红桃，梅花，方块
class Color(Enum):
    SPADE = 1
    HEART = 2
    CLUB = 3
    DIAMOND = 4

# 颜色别名
POKER_COLOR_ALIAS = {
    Color.SPADE: '黑桃',
    Color.HEART: '红心',
    Color.CLUB: '梅花',
    Color.DIAMOND: '钻石'
}
# 和数字映射
POKER_CODE = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

# {value: 'A', color: 1}
class Poker:
    def __init__(self, value, color):
        if value not in POKER_CODE or color not in POKER_COLOR_ALIAS:
            raise ValueError('Poker\'s name or color not found.')
        self.value = value
        self.color = color

    @property
    def code(self):
        return POKER_CODE[self.value]
    @property
    def name(self):
        return POKER_COLOR_ALIAS[self.color] + ' ' + self.value

# 获取最大的牌型组合. 7 选 5
def get_pokers_level(pokers: List[Poker]):
    dic = {}
    level = Level.NO_PAIR
    for poker in pokers:
        value = poker.get_value()
        if dic[value] is None:
            dic[value] = [poker]
        else:
            dic[value].push(poker)
    for d in dic:
        if (len(d) == 2 and level == Level.ONE_PAIR):
            level = Level.TWO_PAIR
        if (
            (len(d) == 3 and level == Level.ONE_PAIR)
            or
            (len(d) == 2 and level == Level.THREE)
        ):
            level = Level.FULL_HOUSE
        if (len(d) == 2):
            level = Level.ONE_PAIR
        if (len(d) == 3):
            level = Level.THREE
        if (len(d) == 4):
            level = Level.FOUR_KIND

# 扑克牌排序（归并排序）
def pokers_sort(pokers):
    if len(pokers) < 2:
        return pokers
    mid = len(pokers) // 2
    l, r = arr[0:mid], arr[mid:]

    def merge(left, right):
        res = []
        while left and right:
            if left[0].get_value() <= right[0].get_value():
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        while left:
            res.append(left.pop(0))
        while right:
            res.append(right.pop(0))

    return merge(pokers_sort(l), pokers_sort(r))

# 合成最大的牌型


def compose_max_poker(pokers):
    count = len(pokers)
    if count < 5:
        return None
    newPokers = []
    for poke in pokers:
        if poke in POKER_CODE:
            newPokers.push(POKER_CODE[poke])
        else:
            newPokers.push(int(POKER_CODE[poke], 10))


# 桌面上的扑克
Z_pokers = [
    Poker('A', Color.SPADE),
    Poker('K', Color.SPADE),
    Poker('Q', Color.SPADE),
    Poker('2', Color.HEART),
    Poker('10', Color.DIAMOND),
]


# Two pair pokers
A_pokers = [
    Poker('A', Color.CLUB),
    Poker('2', Color.DIAMOND)
]

# Three pair pokers
B_pokers = [
    Poker('Q', Color.CLUB),
    Poker('Q', Color.DIAMOND)
]

# No pair pokers
C_pokers = [
    Poker('9', Color.HEART),
    Poker('8', Color.CLUB)
]

# Flush pokers
D_pokers = [
    Poker('5', Color.SPADE),
    Poker('6', Color.SPADE)
]