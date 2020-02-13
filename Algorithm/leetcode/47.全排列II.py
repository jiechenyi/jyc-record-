"""
47.全排列 II

给定一个包含重复数字的全排列，返回所有不重复的全排列
[1,1,2] ---> [1,1,2],[1,2,1],[2,1,1]

和46题相比 就是多了一个去重

"""


def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    if not nums:
        return None
    if len(nums) == 1:
        return [nums]
    if len(nums) == 2:
        tmp = [[nums[0], nums[1]]]
        if [nums[1], nums[0]] not in tmp:
            tmp.append([nums[1],nums[0]])

        return tmp
    if len(nums) > 2:
        tmp = [[nums[0], nums[1]]]
        if [nums[1], nums[0]] not in tmp:
            tmp.append([nums[1], nums[0]])
        j = 2
        while j < len(nums):
            cur = []
            for item in tmp:
                k = len(tmp[0])
                ##遍历每个空位
                for i in range(k + 1):
                    a = item[:]
                    a.insert(i, nums[j])
                    if a not in cur:


                        cur.append(a)
            tmp = cur[:][:]

            j = j + 1
    return tmp

nums=[1,1,2]
print(permuteUnique(nums))


# 递归 + 剪枝

def perm(nums):
    if len(nums) <=1:
        return nums
    nums.sort()
    res=[]

    for i, num in enumerate(nums):
        if i >0 and nums[i-1] == nums[i]:
            continue
        newnums = nums[:i] + nums[i+1:]

        for y in perm(newnums):
            res.append([num]+y)
    return res