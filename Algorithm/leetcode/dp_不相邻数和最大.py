"""
给定数组不能获取相邻的两个数 ，求和最大
注意 第一个元素和倒数第一个元素不能一起用的
"""
class MaxSum(object):
    def f(self,arr):
        if not arr:
            return 0

        n = len(arr)
        # 如果第一个元素要被用到 0~n-1
        dp1 =[0]*n
        dp1[0] = arr[0]
        for i in range(1,n-1):
            dp1[i] = max(dp1[i-2]+arr[i],dp1[i-1])
        a = max(dp1)
        # 如果第一个元素不被用到 1~n
        dp2=[0]*n
   
        for i in range(1,n):
            dp2[i] = max(dp2[i-2]+arr[i],dp2[i-1])
        b = max(dp2)
        return max(a,b)




def maxsum(arr):
    if not arr:
        return 0
    n = len(arr)

    # 使用第一个元素

    dp= [0]*n
    dp[0] = arr[0]

    for i in range(1,n-1):
        dp[i] = max(dp[i-1],dp[i-2]+arr[i])
    a = max(dp)

    # 不使用第一个元素

    dp2 = [0] *n
    for i in range(1,n):
        dp2[i] = max(dp[i-2] + arr[i] , dp[i-1])

    b = max(dp2)

    return max(a,b)

