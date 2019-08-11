"""
837.
给定一个递增的数列，求最长斐波那契数列的长度

"""

def f(arr):
    if not arr:
        return 0
    n = len(arr)
    res = 0
    dp=[[2]*n for _ in range(n)]
    for i in range(1,n):
        l=0
        r=i-1

        while l<r:
            sum = arr[l] +arr[r]
            if sum == arr[i]:
                dp[r][i] = max(dp[r][i],dp[l][r]+1)
                res = max(dp[r][i],res)
                l += 1
                r -=1
            elif sum < arr[i]:
                l += 1
            else:
                r -=1

    return res

arr=[1,3,4,7,10,11,12,18,23,35]
print(f(arr))

#
#
# 将斐波那契式的子序列中的两个连续项 A[i], A[j] 视为单个结点 (i, j)，整个子序列是这些连续结点之间的路径。
#
# 例如，对于斐波那契式的子序列 (A[1] = 2, A[2] = 3, A[4] = 5, A[7] = 8, A[10] = 13)，结点之间的路径为 (1, 2) <-> (2, 4) <-> (4, 7) <-> (7, 10)。
#
# 这样做的动机是，只有当 A[i] + A[j] == A[k] 时，两结点 (i, j) 和 (j, k) 才是连通的，我们需要这些信息才能知道这一连通。现在我们得到一个类似于 最长上升子序列 的问题。
#
# 算法
#
# 设 longest[i, j] 是结束在 [i, j] 的最长路径。那么 如果 (i, j) 和 (j, k) 是连通的， longest[j, k] = longest[i, j] + 1。
#
# 由于 i 由 A.index(A[k] - A[j]) 唯一确定，所以这是有效的：我们在 i 潜在时检查每组 j < k，并相应地更新 longest[j, k]
