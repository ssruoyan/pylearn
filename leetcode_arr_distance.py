# TODO: 目前的思路不对劲，需要重新思考一下
# 已知两个数组 A, B。每次操作能把 A 或者 B 里面的数字 +1 或者 -1。
# 问需要多少次能够使 A 里面的最大值小于等于 B 里面的最小值

def tow_arr_distance(arr1, arr2):
  max_num = max(*arr1)
  min_num = min(*arr2)

  def after_min(num):
    return num > min_num
  def before_max(num):
    return num < max_num

  if (max_num <= min_num): return 0

  arr1_c = list(filter(after_min, arr1))
  arr2_c = list(filter(before_max, arr2))
  
  t1 = 0
  t2 = 0

  for n in arr1_c:
    t1 += abs(n - min_num)
  for n in arr2_c:
    t2 += abs(n - max_num)

  return min(t1, t2)


print(tow_arr_distance([1,2,3,4,5], [1,2,3,4,5]))