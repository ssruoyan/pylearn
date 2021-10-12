# 德州扑克牌型大小比较（德州扑克不区分花色）

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

# 和数字映射
POKER_DICT = {
  'A': 1,
  'J': 11,
  'Q': 12,
  'K': 13
}

# {value: 'A', color: 1, name: '黑桃 A'}
class Poker:
  def __init__(self, value, color, name):
    self.value = value
    self.color = color
    self.name = name
  def get_value(self):
    if self.value in POKER_DICT:
      return POKER_DICT[self.value]
    else:
      return int(self.value, 10)


# 比较两个牌型
def pokers_compare(pokers1, pokers2):

# 获取牌型的等级
def get_pokers_level(pokers):
  dic = {}
  level = Level.NO_PAIR
  for poker in pokers:
    value = poker.get_value()
    if dic[value] is None:
      dic[value] = [poker]
    else:
      dic[value].push(poker)
  for ,d in dic:
    if (len(d) == 2 && level == Level.ONE_PAIR):
      level = Level.TWO_PAIR
    if (
      (len(d) == 3 and level == Level.ONE_PAIR)
      or
      (len(d) == 2 and level == Level.THREE)
    ):
      level = Level.FULL_HOUSE
    if (len(d) === 2):
      level = Level.ONE_PAIR
    if (len(d) === 3):
      level = Level.THREE
    if (len(d) === 4):
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
    if poke in POKER_DICT:
      newPokers.push(POKER_DICT[poke])
    else:
      newPokers.push(int(POKER_DICT[poke], 10))

# 桌面上的扑克
p_pokers = [
  Poker('A', Color.SPADE, '黑桃 A'),
  Poker('K', Color.SPADE, '黑桃 K'),
  Poker('Q', Color.SPADE, '黑桃 Q'),
  Poker('2', Color.HEART, '红心 2'),
  Poker('10', Color.DIAMOND, '方块 10'),
]


# Two pair pokers
A_pokers = [
  Poker('A', Color.CLUB, '梅花 A')
  Poker('2', Color.DIAMOND, '方块 2')
]

# Three pair pokers
B_pokers = [
  Poker('Q', Color.CLUB, '梅花 Q')
  Poker('Q', Color.DIAMOND, '方块 Q')
]

# No pair pokers
C_pokers = [
  Poker('9', Color.HEART, '红心 Q'),
  Poker('8', Color.CLUB, '梅花 8')
]

# Flush pokers
D_pokers = [
  Poker('5', Color.SPADE, '黑桃 9'),
  Poker('6', Color.SPADE, '黑桃 6')
]

