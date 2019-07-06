
"""
将0 移到数组的最后，切不改变数组中数字原有的顺序
"""

## 我的解法
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <=1:
            return nums
        l = 0
        r = 1
        while l<r and r<len(nums):
            if nums[l] == 0 and nums[r]!=0:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
                l+=1
                r +=1
            elif nums[l] != 0 and nums[r] == 0:
                l+=1
                r+=1
            elif nums[l] ==0 and nums[r] == 0:
                r+=1
            elif nums[l] !=0 and nums[r] !=0:
                l+=1
                r+=1
                
        return nums

## 法2

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                if count !=i:
                    nums[i] =0
                count +=1
        return nums
        