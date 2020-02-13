"""
75.颜色分类（荷兰国旗问题）

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。



"""

def sortColors(nums):
    # 先把 2 移到最后

    n = len(nums)
    big = 0
    while big < n:
        if nums[big] == 2:
            right = big
            while right< n:
                if nums[right] != 2:
                    tmp = nums[right]
                    nums[right] = nums[big]
                    nums[big] = tmp

                    big += 1
                    break
                else:
                    right += 1
            if right >= n:
                break
        else:
            big += 1
    # 再把0移到最前面
    small = n-1
    while small >=0:
        if nums[small] == 0:
            left = small
            while left >= 0:
                if nums[left] != 0:
                    tmp = nums[left]
                    nums[left] = nums[small]
                    nums[small] = tmp

                    small -= 1
                    break
                else:
                    left -= 1
            if left < 0:
                break
        else:
            small -=1
    return nums

nums = [2,0,2,1,1,0]
print(sortColors(nums))

def sortColors(nums):
    
    cur = 0  # 当前位置
    
    low = 0 # 记录0出现过的位置
    
    hi = len(nums) -1 # 记录2 应该在的位置 
    
    while cur <= hi:
        if nums[cur] == 0  and cur == low :
            cur +=1
            low += 1
        elif nums[cur] == 0 and low < cur:
            nums[cur],nums[low] = nums[low], nums[cur]
            cur += 1
            low += 1
        elif nums[cur] == 1 : 
            cur +=1
        elif nums[cur] == 2:
            nums[cur],nums[hi] = nums[hi], nums[cur]
            hi -=1

nums=[2,0,2,1,1,0 ]
print(sortColors(nums))
    
            
            






























    #
    #
    # cur = 0
    # low = 0
    # hi = len(nums) - 1
    # while cur <= hi:
    #     if nums[cur] == 0 and cur == low:
    #         cur += 1
    #         low += 1
    #     elif nums[cur] == 0 and low < cur:
    #         tmp = nums[cur]
    #         nums[cur] = nums[low]
    #         nums[low] = tmp
    #         low += 1
    #         cur += 1
    #     elif nums[cur] == 1:
    #         cur += 1
    #     elif nums[cur] == 2:
    #         tmp = nums[cur]
    #         nums[cur] = nums[hi]
    #         nums[hi] = tmp
    #         hi -= 1
    # print(nums)
    #
    #
    #
