def intToRoman( num):
    """
    :type num: int
    :rtype: str
    """
    if not num:
        return
    res = ''
    dic = {1: 'I', 5: 'V', 10: 'X', 50: "L", 100: 'C', 500: 'D', 1000: 'M'}
    if num // 1000 and num >= 1000:
        qian = num // 1000
        res += "M" * (qian)
        num = num - qian * 1000
    if num // 100 and num >= 100:
        bai = num // 100
        if bai == 4:
            res += "CD"
            num = num - 400
        elif bai == 9:
            res += "CM"
            num = num - 900
        elif bai >= 5:
            res = res + 'D' * 1 + "C" * (bai - 5)
            num = num - bai * 100
        else:
            res += 'C' * bai
            num = num - bai * 100
    if num // 10 and num >= 10:
        shi = num // 10
        if shi == 4:
            res += "XL"
            num = num - 40
        elif shi == 9:
            res += "XC"
            num = num - 90
        elif shi >= 5:
            res = res + 'L' * 1 + "X" * (shi - 5)
            num = num - shi * 10
        else:
            res += "X" * shi
            num = num - shi * 10
    if num == 5:
        res += "V"
    elif num == 4:
        res += 'IV'
    elif num == 9:
        res += "IX"
    elif num > 5:
        res = res + 'V' + (num - 5) * "I"
    elif num < 5:
        res = res + num * "I"
    return res


"""

别人优雅的代码
"""


def intToRoman(num: int) -> str:
    rome = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }
    compare = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ans = ""
    i = 0
    while num != 0:
        while num >= compare[i]:
            ans += rome[compare[i]]
            num -= compare[i]
        i += 1
    return ans




