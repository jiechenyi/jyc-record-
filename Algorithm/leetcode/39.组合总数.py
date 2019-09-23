"""


39.组合总数
从 candidates 里面选择元素 使得加起来等于 target
元素可以重复用，但是组合不可以重复
"""

class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []

        def helper(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            helper(i, tmp_sum + candidates[i], tmp + [candidates[i]]) # 用这个candidate
            helper(i + 1, tmp_sum, tmp) # 不用这个candidate

        helper(0, 0, [])
        return res

def f(candidates,target):
    candidates.sort()
    n = len(candidates)
    res=[]

    def helper(start,candidates,target,tmp):
        if target < 0:
            return
        if target == 0:
            res.append(tmp)
            return
        else:
            for i in range(start,n):
                tmp += [candidates[i]]
                tmp_sum = sum(tmp)
                helper(i,candidates,target-tmp_sum,tmp)
                tmp = tmp[:-1]

    helper(0,candidates,target,[])
    return res

candidates=[2,3,6,7]
target = 7

print(f(candidates,target))
