"""

最长上升子序列的长度
"""
class Solution(object):
    """
    子序列
    
    """
    def f(self,arr):
        n = len(arr)
        dp=[1]*n

        for i in range(1,n):
            for j in range(i,-1,-1):
                if arr[i] >=arr[j]:
                    dp[i]= max(dp[j]+1,dp[i])
        return max(dp)
    """
    子串
    """
    def f2(self,arr):
        n = len(arr)
        dp=[1]*n
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                dp[i] = max(dp[i-1]+1,1)
        return max(dp)


def maxlen(arr):
    if not arr:
        return
    n = len(arr)
    dp = [1]*n
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if arr[i]> arr[j]:
                dp[i]  = max(dp[i],dp[j]+1)
    return max(dp)
        