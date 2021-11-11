from typing import List

def move_zeroes(nums: List[int]):
  count = 0
  ln = len(nums)
  while(ln > 1 and nums[ln - 1] == 0):
      ln = ln - 1
  if (ln <= 1): return nums
  for i in range(0, ln):
    if (nums[i] == 0):
      count = count + 1
    else:
      nums[i - count] = nums[i]
  for j in range(ln - count, ln):
    nums[j] = 0
  return nums

def move_zeroes1(nums):
  ln = len(nums)
  l = 0
  for i in range(0, ln):
    if (nums[i] != 0):
      if (i != l):
        nums[i], nums[l] = nums[l], nums[i]
      l = l + 1
  return nums
print(move_zeroes1([0, 3,4,0,5,1,0,9,0,9]))

