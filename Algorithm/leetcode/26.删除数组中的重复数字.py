def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return
    if len(nums) == 1:
        return 1
    if len(nums) == 2:
        if nums[0] == nums[1]:
            return 1
        else:
            return 2
    else:
        n = len(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i-1)
            else:
                i +=1
        return len(nums)

nums =[2,2,2,3,4]
removeDuplicates(nums)