"""
77.组合

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

"""

# 解法一：排列组合的性质
#  C(m,n)=C(m-1,n)+C(m-1,n-1)
def combine(n,k):
    if k>n:
        return []

    if k == 1:
        return [[i] for i in range(1,n+1)]
    if k == n:
        return [list(range(1,n+1))]

    res = combine(n-1, k)

    for item in combine(n-1, k-1):
        res.append(item+[n])
    return res
n = 4
k=2

print(combine(n,k))

# 回溯法

def combine2(n, k):
    res=[]
    def backtrack(first, cur):
        if len(cur) == k:
            res.append(cur[:])
        for i in range(first, n+1):
            cur.append(i)

            backtrack(i+1, cur)

            cur.pop()

    backtrack()

    return res

