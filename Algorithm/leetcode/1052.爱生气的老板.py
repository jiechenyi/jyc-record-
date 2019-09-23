"""

1052.爱生气的老板

今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。

请你返回这一天营业下来，最多有多少客户能够感到满意的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def maxSatisfied(customers, grumpy, X):
    """
    :type customers: List[int]
    :type grumpy: List[int]
    :type X: int
    :rtype: int
    """
    n = len(customers)

    tmp = 0
    for i in range(n):
        if grumpy[i] == 0:
            tmp += customers[i]


    i = 0
    profit = 0
    for j in range(i + X):
        if grumpy[j] == 1:
            profit += customers[j]
    i += 1
    maxnum = profit

    while i + X - 1 < n:
        if grumpy[i + X - 1] == 1:
            profit += customers[i + X - 1]
        if grumpy[i-1] == 1:
            profit -= customers[i-1]

        maxnum = max(maxnum, profit)
        i += 1
    return tmp + maxnum

customers=[1,0,1,2,1,1,7,5]
grumpy =[0,1,0,1,0,1,0,1]
X= 3

print(maxSatisfied(customers,grumpy,X))



