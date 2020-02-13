'''

29.两数相除
不能使用乘法、除法、mod等操作

'''


def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """

    if dividend == 0:
        return 0

    d1 = abs(dividend)
    d2 = abs(divisor)

    cur = d2
    i=1

    a = []
    b =[]

    while cur <= d1:
        a.append(cur)
        b.append(i)
        cur += cur # 以 1，2，4，8，的倍数增长
        i += i


    res =0

    for j in range(len(a)-1, -1, -1):  # 从大到小找，其实就是手动实现 竖式相除
        if a[j] <= d1:
            res += b[j]
            d1 -= a[j]



    if dividend < 0 and divisor <0 :
        pass
    elif dividend >0 and divisor >0 :
        pass
    else:
        res = -res

    if res > 2**31-1:
        return 2**31 -1
    if res< -2**31:
        return -2**31








# 思考：应该可以用 递归 来解决



dividend = -2147483648
divisor = -1
print(divide(dividend,divisor))