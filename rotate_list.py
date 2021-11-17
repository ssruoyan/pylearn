from typing import List

def rotate_list(nums: List[int], k):
    n = len(nums)
    if k == 0: return nums
    if k > n: k = k % n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    print(nums)

def reverse(nums, start, end):
    while(start < end):
        nums[start], nums[end] = nums[end], nums[start]
        start = start + 1
        end = end - 1
    
rotate_list([1,2, 3,4,5,6,7], 5)

def reverse_words(s):
    arr = s.split(' ')
    arr.reverse()
    print(arr)
    i = len(arr) - 1
    while(i >= 0):
        arr[i] = arr[i][::-1]
        i = i - 1
    return ' '.join(arr)

print(reverse_words('1234 5678'))