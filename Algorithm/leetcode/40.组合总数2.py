"""

40.组合总数
不能重复取一个数字

"""


def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if not candidates:
        return
    candidates.sort()
    n = len(candidates)
    res = []

    def help(i, tmp_sum, tmp):
        if tmp_sum == target:
            res.append(tmp)
            return
        for j in range(i, n):
            if tmp_sum + candidates[j] > target:
                break
            if j > i and candidates[j] == candidates[j - 1]:
                continue
            help(j + 1, tmp_sum + candidates[j], tmp + [candidates[j]])

    help(0, 0, [])
    return res


candidates= [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates,target))