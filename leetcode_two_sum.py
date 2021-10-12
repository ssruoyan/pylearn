# 两数之和。给定一个整数数组 nums 和目标值 target
# 在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标
class Solution:
    # 枚举方法
    def two_sum(self, nums, target):
      i = 0
      j = 1
      length = len(nums)
      while i <= length - 2:
        print(i, j)
        if (nums[i] + nums[j] == target):
          return [i, j]
        elif j >= length - 1:
          i = i + 1
          j = i + 1
        else:
          j += 1
      
      return [0]
    
    # 字典方法
    def two_sum2(self, nums, target):
      dict = {}
      for idx, num in enumerate(nums):
          if target - num in dict:
            return [idx, dict[target - num]]
          dict[num] = idx
      return [0]

print(Solution().two_sum2([2,1,8,7,11,15], 9))