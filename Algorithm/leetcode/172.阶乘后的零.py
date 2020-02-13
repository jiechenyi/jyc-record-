"""
172.阶乘后的零

给定一个整数 n，返回 n! 结果尾数中零的数量。
"""


def trailingZeroes( n):
    """
    :type n: int
    :rtype: int
    """

    res = 0

    while n>0:
        res += n/5
        n = n/5

    return res

n=30
print(trailingZeroes(n))