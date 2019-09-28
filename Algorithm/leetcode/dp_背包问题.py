"""

假设有 n件物品，每件物品的重量和价值分别存为 w 和 v
背包的容量是 m
请问背包可以装下的最大价值是多少

"""

def f(w,v,m):
    n = len(w)

    dp =[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if j < w[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-w[i]]+v[i])
    return dp[-1][-1]


"""
多背包问题
每个物品的件数，存放在 p 中

"""

def f1(w,v,m,p):
    n = len(w)
    dp = [[0]*(m+1) for _ in range(n+1)]
    # j 代表 容量
    # i 代表 物品的 index
    for i in range(n + 1):
        for j in range(m+1):

            if j < w[i] :
                dp[i][j] = dp[i-1][k]
            else:
                for k in range(1,p[i]):
                    dp[i][j] = max(dp[i][j],dp[i-1][j-k*w[i]]+k*v[i])
    return dp[-1][-1]


"""
完全背包问题
每个物品有无穷多件
"""

def f3(w,v,m):
    n = len(w)
    dp=[[0]*(m+1) for _ in range(n+1)]
    for j in range(m+1):
        for i in range(n+1):
            if j < w[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-w[i]]+v[i])
    return dp[-1][-1]
