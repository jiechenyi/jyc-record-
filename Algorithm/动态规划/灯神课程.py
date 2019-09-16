"""
工作时长

每个工作有它需要完成的时间和报酬
求最大能获得多少报酬


"""


"""
和最大
不能选相邻的，使得选出来的数字加起来和最大

"""

arr=[1,2,4,1,7,8,3]
def maxsum(arr):
    n = len(arr)
    dp=[0]*n
    dp[0] = arr[0]
    dp[1] = max(arr[0],arr[1])
    for i in range(2,n):
        dp[i] = max(dp[i-1],dp[i-2]+arr[i])
    return dp[-1]

"""
加起来等于target

"""
