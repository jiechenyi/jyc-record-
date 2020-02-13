"""
167.两数之和II- 输入有序数组

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

"""

# 因为已经有序了 所以双指针 不然会超时

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    left = 0
    right = len(numbers)-1

    while left<= right:
        tmp = numbers[left] + numbers[right]
        if tmp == target:
            return [left+1, right+1]
        elif tmp > target:
            right -= 1
        elif tmp < target:
            left += 1
    return





numbers =[3,24,50,79,88,150,345]
target = 200
print(twoSum(numbers, target))