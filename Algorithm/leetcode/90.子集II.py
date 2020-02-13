"""
90.子集II
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集
"""

def subsetsWithDup(nums):
    nums.sort()
    def helper(res, nums, re):
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            sub = re + [nums[i]]
            res.append(sub)
            helper(res, nums[i + 1:], sub)
    res = [[]]
    helper(res, nums, [])
    return res



nums=[1,2,2]
print(subsetsWithDup(nums))

