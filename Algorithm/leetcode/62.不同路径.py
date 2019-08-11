"""
62.不同路径

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？


"""

def uniquePaths(m, n):
    dp=[ [0]*m for _ in range(n)]
    for i in range(m):
        dp[0][i] = 1
    for j in range(n):
        dp[j][0] =1
    for i in range(1,m):
        for j in range(1,n):
            dp[j][i] = dp[j][i-1]+dp[j-1][i]
    return dp[-1][-1]

m=7
n=3
print(uniquePaths(m,n))