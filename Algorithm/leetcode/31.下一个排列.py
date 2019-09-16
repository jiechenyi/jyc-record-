"""

31.下一个排列
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""


def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if not nums:
        return
    n = len(nums)
    flag = 0
    for k in range(1, n):
        if nums[k - 1] >= nums[k]:
            flag = 0
        else:
            flag = 1
            break
    if flag == 0:
        print( nums[::-1])

    n = len(nums)

    for i in range(n-1,-1,-1):
        if nums[i-1] < nums[i]:
            for j in range(n-1,i-1,-1):
                if nums[j] > nums[i-1]:
                    tmp = nums[j]
                    nums[j] = nums[i-1]
                    nums[i-1] = tmp
                    break
                else:
                    continue
            break
        else:
            continue


    res = inverse(nums,i,len(nums)-1)# 对排序再改进一下

    return res

def inverse(nums,start,end):
    if start < end:
        m = (end-start+1)//2
        for i in range(start,start+m,1):
            tmp = nums[i]
            nums[i] = nums[end-(i-start)]
            nums[end-(i-start)] = tmp
    return nums




nums =[1,3,2]
print(nextPermutation(nums))



