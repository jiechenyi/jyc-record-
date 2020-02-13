"""
80.删除排序数组中的重复项II

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。


"""

def removeDuplicates(nums):


    flag = 1

    i = 0
    while i < len(nums):
        if i > 0 and nums[i] == nums[i-1]:
            flag += 1
        if i>0 and nums[i] != nums[i-1]:
            flag = 1

        if flag > 2:
            nums.pop(i)
            flag -=1

        else:
            i+=1
    return nums

nums=[1,1,1,1]
print(removeDuplicates(nums))


# 因为题目要求返回 修改后的数组的长度
def removeDuplicates2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    for e in nums:
        if i < 2 or e != nums[i - 2]:
            nums[i] = e
            i += 1

    return i
nums=[1,1,1,2,2,3]
print(removeDuplicates2(nums))