"""
873.
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
                dp[r][i] = max(dp[r][i], dp[l][r]+1)
                res = max(dp[r][i], res)
                l += 1
                r -=1
            elif sum < arr[i]:
                l += 1
            else:
                r -=1

    return res

arr=[1,3,4,7,10,11,12,18,23,35]






def lenLongestFibSubseq(A):
    if not A:
        return 0

    n = len(A)
    res = 0

    dp = [[2] * n for _ in range(n)] # dp[i][j] 表示以 A[i] A[j] 结尾的数列的长度

    for i in range(1,n):
        left = 0  # 在0～ i-1 中寻找加起来等于 A[i]的数列
        right = i-1

        while left < right:
            sum = A[left] + A[right]
            if sum == A[i]:

                dp[right][i] = max(dp[right][i], dp[left][right]+1) # 在原本 left->right 的基础上 加了一个 i，所以是 dp[left][right] +1 
                res = max(dp[right][i], res)

                right -= 1
                left += 1
            elif sum < A[i]:
                left += 1
            else:
                right -= 1
    return res

A = [1,2,3,4,5,6,7,8]
print(lenLongestFibSubseq(A))



































