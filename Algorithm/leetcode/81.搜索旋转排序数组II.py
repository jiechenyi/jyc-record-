"""

  81.搜索旋转排序数组II

  假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。


"""

def search(nums, target):
    n = len(nums)
    p = n
    for i in range(n):
        if i>0 and nums[i] < nums[i-1]:
            p = i
            break

    def bs(left,right):


        while left<=right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return False
    if target == nums[0]:
        return True
    if target > nums[0]:
        return bs(0, p-1)
    if target < nums[0]:
        return bs(p,n-1)

nums = [1,3]
target = 3

print(search(nums,target))