"""
超典型！！
强烈推荐

322.零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

"""

# dp
# dp[i] 表示凑成i元所需要的最小硬币个数


def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    if not amount:
        return 0

    n = len(coins)

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for m in range(1, amount + 1):
        for i in range(n):
            if coins[i] <= m:
                dp[m] = min(dp[m], dp[m - coins[i]] + 1)  # 取或者不取
    if dp[-1] != float('inf'):
        return dp[-1]
    else:
        return -1


