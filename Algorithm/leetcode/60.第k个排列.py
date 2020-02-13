"""


60.第k个排列

给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

"""
# 思路：
# 一一定位
# 因为假设固定第一个数 那么余下的数字会有(n-1)!种的排列方式
# 也就是说所有排列是有规律的，这个规律就是 每(n-1)!个数的第一个数字都是一样的
# 这样用 k/(n-1)! 就可以知道第k个排列是在哪组里
#
# 找到组后 把这个数字（也就是组号）从需要排列的list中剔除掉
# 对于余下的重复上述的过程即可

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number*factorial(number-1)

def getPermutation(n, k):


    ll = list(range(1,n+1))

    res=''
    while len(ll) >2:
        nn = len(ll)
        f = factorial(nn-1)
        shang = int(k/f)
        yu = k - shang * f
        if yu == 0:
            shang = shang-1

        k = yu
        res += str(ll[shang])


        ll.pop(shang)


    if k == 1:
        for i in ll:
            res += str(i)
    else:
        for i in ll[::-1]:
            res += str(i)
    return res
n = 3
k= 2

print(getPermutation(n,k))