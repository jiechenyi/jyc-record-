"""
518.（有一个目标值，一个arr ，arr里的coin可以使用任意多次，求凑成目标值的方法数）
"""

def f(amount,arr):
    n = len(arr)
    dp = [[0]*(amount+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] =1
    for j in range(amount+1):
        if amount % arr[0] ==0:
            dp[0][j] =1
    for i in range(1,n):
        for j in range(1,amount+1):
            if j>=arr[i]:
                # 不用上这个coin ，和用这个coin
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

