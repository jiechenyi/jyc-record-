"""
518.（有一个目标值，一个arr ，arr里的coin可以使用任意多次，求凑成目标值的方法数）
"""

def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    if not coins and amount != 0:
        return 0
    if not coins:
        return 1
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n)]
    for i in range(amount + 1):
        if i % coins[0] == 0:
            dp[0][i] = 1
    for j in range(n):
        dp[j][0] = 1
    for i in range(1, n):
        for j in range(1, amount + 1):

            if j >= coins[i]:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]


amount=7
arr=[2,3,6,7]
print(f(amount,arr))



def change_(amount,coins):
    n = len(coins)
    coins.sort()

    dp=[[0]*(amount+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for j in range(1,amount+1):
        if j % coins[0] == 0:
            dp[0][j] = 1
    for i in range(1,n):
        for j in range(1,amount+1):
            if j < coins[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] =dp[i-1][j] + dp[i][j-coins[i]]
    return dp[-1][-1]