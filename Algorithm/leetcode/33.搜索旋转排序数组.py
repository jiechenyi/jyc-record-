def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    def binarySearch(l, r):

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                return mid
        return -1

    if not nums:
        return -1

    rotate_index=0
    l = 0
    r = len(nums)-1
    if nums[l] < nums[r]:
        rotate_index=0
    else:
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1] :
                rotate_index=\
                    mid+1
                break
            else:
                if nums[mid] < nums[l] :
                    r = mid-1


                else:
                    l = mid+1


    if nums[rotate_index] == target:
        return rotate_index
    if rotate_index == 0:
        return binarySearch(0,len(nums-1))
    if target < nums[0]:
        return binarySearch(rotate_index,len(nums)-1)
    return binarySearch(0,rotate_index)


nums =[3,1]
target=3
print(search(nums,target))



# 官方题解
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def search(left, right):
            """
            Binary search
            """
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        n = len(nums)

        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)

        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)
        # search on the left side
        return search(0, rotate_index)

