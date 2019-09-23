"""

34.在排序数组中查找元素的第一个和最后一个位置


"""


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if not nums:
        return [-1, -1]
    if nums[0] > target:
        return [-1, -1]
    n = len(nums)
    res = [-1, -1]
    left = 0
    right = n - 1
    if n ==1 and nums[0] == target:
        return [0,0]
    tmp0 =99999
    # 找到最左边的
    while left <= right:
        tmp0 = min(tmp0, help(nums, left, right, target, "min"))
        right = right-1

    if tmp0 == 99999:
        return [-1,-1]
    res[0] = tmp0
    left = tmp0
    right = n-1


    # 找到最右边的
    tmp1 = -1
    while left <= right:
        tmp1 = max(tmp1, help(nums,left, right, target, "max"))


        left = left+1

    if tmp1 == -1:
        return [-1,-1]


    res[1] = tmp1

    return res
# 二分查找

def help(nums,l,r,target,flag):
    if l > r:
        if flag == "min":
            return 99999
        if flag == "max":
            return -1


    mid = (l+r) //2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return help(nums,l,mid-1,target,flag)
    elif nums[mid] < target:
        return help(nums,mid+1,r,target,flag)





nums=[2,2]

target = 2

print(searchRange(nums,target))