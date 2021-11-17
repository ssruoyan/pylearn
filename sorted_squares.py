from typing import List

def sorted_squares1(nums: List[int]) -> List[int]:
    l, r = 0, len(nums) - 1
    while(l < r):
        left = nums[l] * nums[l]
        right = nums[r] * nums[r]
        if (left > right):
            nums[l], nums[r] = nums[r], left
            r = r - 1
        elif left < right:
            nums[r] = right
            r = r - 1
        else:
            nums[l], nums[r - 1] = nums[r - 1], left
            nums[r] = right
            r = r - 2
        print(nums)
    return nums

def sorted_squares(nums: List[int]) -> List[int]:
    n = len(nums)
    l, r = 0, n - 1
    arr = [0] * n
    left = -1
    right = -1
    while(l < r):
        if (left == -1): left = nums[l] * nums[l]
        if (right == -1): right = nums[r] * nums[r]

        if (left > right):
            arr[r - l] = left
            left = -1
            l = l + 1
        elif left < right:
            arr[r - l] = right
            right = -1
            r = r - 1
        else:
            arr[r - l] = right
            arr[r - l - 1] = left
            left = -1
            right = -1
            l = l + 1
            r = r - 1
    if (l == r): arr[0] = nums[l] * nums[l]
    return arr

print(sorted_squares([-4, -1, 0, 0, 3, 10]))