def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if len(nums) < 4:
        return
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        else:
            cha = target - nums[i]
            tmp = threeSum(nums[i + 1:], cha)
            if tmp:
                tmp_ = [_.append(nums[i]) for _ in tmp]
                for item in tmp:
                    item.sort()
                    if item not in res:
                        res.append(item)

    return res


def threeSum(nums, target):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return
    nums.sort()
    res = []
    n = len(nums)
    i = 0

    while i < n:
        if nums[i] > nums[i - 1] or i == 0:
            j = i + 1
            m = n - 1

            while j < m:
                sum = nums[i] + nums[j] + nums[m]
                if sum < target:
                    j += 1
                elif sum > target:
                    m -= 1
                elif sum == target:
                    res.append([nums[i], nums[j], nums[m]])
                    j += 1
                    m -= 1
                    # 以下在实现去重逻辑

                    while j < m and nums[j] == nums[j - 1]:
                        j += 1
                    while j < m and nums[m] == nums[m + 1]:
                        m -= 1

        i += 1

    return res


nums=[5,5,3,5,1,-5,1,-2]
target=4
fourSum(nums,target)

