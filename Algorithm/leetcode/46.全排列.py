"""
46.全排列
没有重复数字的数组，写出它的全排列

"""
# 递归
def perm(nums):
    if len(nums) <=1:
        return [nums]

    res=[]
    for i, num in enumerate(nums):
        newnums = nums[:i] + nums[i+1:]

        for y in perm(newnums):
            res.append([num]+y)
    return res

nums=[1,2,3,4]

perm(nums)