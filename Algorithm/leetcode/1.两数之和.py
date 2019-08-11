def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if not nums:
        return
    dic = {}
    for index, i in enumerate(nums):
        cha = target-i
        if dic.get(cha):
            return [dic[target - i]-1, index]
        else:
            dic[i] = index+1
    return

nums=[2,7,11,15]
target=9
twoSum(nums,target)