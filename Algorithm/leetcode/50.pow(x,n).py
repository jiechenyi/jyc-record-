"""
50.pow(x, n)

实现 pow(x, n) ，即计算 x 的 n 次幂函数
"""


def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """

    if n == 1:
        return x
    if n == 2:
        return x * x
    if n < 0:
        m = abs(n)
        return myPow(1 / x, m)
    if n == 0:
        return 1

    shang = int(n / 2)

    yu = n % 2
    if yu == 0:
        return myPow(x, shang) ** 2
    else:

        return x * myPow(x, shang) ** 2



x=0.00001
n=2147483647

print(myPow(x,n))