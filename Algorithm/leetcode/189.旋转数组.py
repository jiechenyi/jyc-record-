"""
189.旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数
"""

# 要用3种方法

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if k == 0:
        return nums
    m = k % n
    while m > 0:
        tmp = nums.pop()
        nums.insert(0, tmp)
        m -= 1

#

def rotate2(nums,k):
    for i in range(k):
        previous = nums[len(nums)-1]
        for j in range(len(nums)):
            tmp = nums[j]
            nums[j] = previous
            previous = tmp
    return nums

nums= [1,2,3,4,5,6]
k=3

print(rotate2(nums,k))

def rotate3(nums,k):
    n = len(nums)
    if k == 0:
        return nums
    m = k % n
    tmp = nums[-m:] + nums[:-m]

    nums[:] = tmp[:]
    print(nums)
