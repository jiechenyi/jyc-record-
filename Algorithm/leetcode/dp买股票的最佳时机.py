
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        
        dp=[0]*len(prices)
        minp= prices[0]
        
        for i in range(1,len(prices)):
            if prices[i-1] <minp:
                minp = prices[i-1]
            dp[i] = prices[i] - minp
        return max(dp)



def maxp(prices):
    n = len(prices)
    dp = [0]*n
    minp = prices[0]
    for i in range(1,n):
        if prices[i-1] < minp:
            minp = prices[i-1]  # 找到i 之前 最小的价格
        dp[i] = prices[i] - minp
    return max(dp)