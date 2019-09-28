"""
最长公共子序列
"""
def f(a,b):
    if not a or b:
        return 
    n = len(a)
    m= len(b)

    dp =[[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return dp[-1][-1]



def maxlen(a,b):
    if not a or b :
        return
    n = len(a)
    m = len(b)

    dp =[[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]



    

