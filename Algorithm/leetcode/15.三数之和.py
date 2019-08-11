
"""

15.三个数加起来等于0

"""
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return
    nums.sort()
    res = []
    n = len(nums)
    i = 0

    while i < n:
        if nums[i] > nums[i - 1] or i == 0:
            j = i + 1
            m = n - 1

            while j < m:
                sum = nums[i] + nums[j] + nums[m]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    m -= 1
                elif sum == 0:
                    res.append([nums[i], nums[j], nums[m]])
                    j += 1
                    m -= 1
                    # 以下在实现去重逻辑

                    while j < m and nums[j] == nums[j - 1]:
                        j += 1
                    while j < m and nums[m] == nums[m + 1]:
                        m -= 1

        i += 1

    return res


nums=[-1, 0, 1, 2, -1, -4]
threeSum(nums)
