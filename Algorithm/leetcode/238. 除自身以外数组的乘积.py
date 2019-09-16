
"""
238.
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。



"""


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    if not nums:
        return
    res = []

    left = [1] * len(nums)
    right = [1] * len(nums)
    # left[0] = nums[0]
    left[1] = nums[0]
    # right[-1] = nums[-1]
    right[-2] = nums[-1]

    # 计算这个数字左边和右边的乘积
    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]
    print(left)

    for j in range(len(nums) - 3, -1, -1):
        right[j] = right[j + 1] * nums[j + 1]
    print(right)
    for k in range(len(nums)):
        res.append(left[k]*right[k])
    return res

nums=[1,2,3,4,5,6]
print(productExceptSelf(nums))