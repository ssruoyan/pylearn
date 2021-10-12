import time

# 暴力递归
def drop_egg(N, K):
  def dp(n, k):
    if k == 1 or n == 1 or n == 0:
      return n
    m = n
    for i in range(1, n + 1):
      m1 = 1 + max(dp(i - 1, k - 1), dp(n - i, k))
      m = min(m, m1)
    return m
  return dp(N, K)

# 表记忆优化递归
def drop_egg_hash(N, K):
  memo = {}
  def dp(n, k):
    if (n, k) in memo:
      return memo[n, k]
    if k == 1 or n == 1 or n == 0:
      memo[n, k] = n
      return n
    m = n
    for i in range(1, n):
      m1 = 1 + max(dp(i - 1, k - 1), dp(n - i, k))
      m = min(m, m1)
    memo[n, k] = m
    return m
  return dp(N, K)

# 二分查找初始楼层
def drop_egg_binary(N, K):
  memo = {}
  def dp(n, k):
    if (n, k) in memo:
      return memo[n, k]
    if k == 1 or n == 1 or n == 0:
      memo[n, k] = n
      return n
    # 二分查找开始。离散点查找 low, high, middle
    low = 1
    high = n
    while low + 1 < high:
      middle = (low + high) // 2
      # 取左右两边的值比较
      lValue = dp(middle - 1, k - 1)
      rValue = dp(n - middle, k)
      
      if lValue < rValue:
        low = middle
      elif lValue > rValue:
        high = middle
      else:
        low = high = middle
    m = 1 + min(
      dp(n - low, k),
      dp(high - 1, k - 1)
    )
    memo[n, k] = m
    return m
  return dp(N, K)

def drop_egg_func(n, k):
  # dp[x] = drop_egg_func(x, 1) 一个鸡蛋情况
  dp = list(range(n + 1)) # t1
  dp2 = [0] * (n + 1) # t2
  # 从第二个鸡蛋开始
  for i in range(2, k + 1):
    # 开始楼层
    x = 1
    for j in range(1, n + 1):
      # max(t1(x - 1), t2(x - 1) > max(t1(x), t2(x)))
      while x < j and max(dp[x - 1], dp2[j - x]) > max(dp[x], dp2[j - x - 1]):
        x += 1
      dp2[j] = 1 + max(dp[x - 1], dp2[j - x])
    dp = dp2[:]
  return dp[-1]