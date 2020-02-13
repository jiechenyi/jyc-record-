"""
69.X的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去
"""

# 牛顿法

def mySqrt(x):

    cur = x
    while cur**2>x:

        cur = (cur + x/cur)//2

    return int(cur)



x = 8
print(mySqrt(x))

# 二分法

def mySqrt2(x):
    if x <=1 :
        return x

    left =1
    right = x//2

    while left <= right:
        mid = left + (right-left)//2

        if mid > x/mid:
            right = mid -1
        else:
            left = mid +1


    return left - 1
