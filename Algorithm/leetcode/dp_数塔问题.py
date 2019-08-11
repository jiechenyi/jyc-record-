"""
三角形 从上到下的最小路径和

"""

def f(arr):
    dp=arr[:][:]
    n = len(arr)
    for i in range(1,n):
        for j in range(len(arr[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j]+arr[i][j]
            elif j == len(arr)-1:
                dp[i][j] = dp[i-1][j-1]+arr[i][j]
            else:
                dp[i][j] = min(dp[i-1][j-1]+arr[i][j],dp[i-1][j]+arr[i][j])
    return min(dp[-1])           
            