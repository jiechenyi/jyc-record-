"""
66.加一

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

"""


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    l = len(digits)

    res=[]
    flag=1
    while digits:
        if digits[-1] == 9 and flag==1:
            digits.pop(-1)
            res.insert(0,0)
            flag = 1
        elif flag==1:
            tmp = digits.pop(-1)
            res.insert(0, tmp+1)
            flag = 0
        else:
            tmp = digits.pop(-1)
            res.insert(0, tmp)
    if flag ==1:
        res.insert(0,1)
    return res

digits=[9,9,9,9,9]
print(plusOne(digits))




