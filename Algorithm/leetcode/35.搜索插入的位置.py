
"""
35.搜索插入的位置
排序序列nums ，target
找到target的话 返回 索引
否则 返回应该插入的位置
"""


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums:
        return

    left = 0
    right = len(nums) -1
    while left <= right:
        mid = (left+right) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
    return left
