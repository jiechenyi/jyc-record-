"""

22.给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

"""


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    if not n:
        return
    res = []
    help(res, "", 0, 0, n)
    return res


def help(res, tmp, count1, count2, n):
    if count1 > n or count2 > n:
        return
    if count1 == n and count2 == n:
        res.append(tmp)
    if count1 >= count2:
        tmp1 = tmp[:]
        help(res, tmp + '(', count1 + 1, count2, n)
        help(res, tmp1 + ')', count1, count2 + 1, n)

n =3
generateParenthesis(n)