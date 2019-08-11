"""

17
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


"""

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return
    dic = {"2": 'abc', "3": 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits) == 1:
        return list(dic[digits])

    s = []
    for i in digits:
        s.append(dic[i])
    res = []

    n = len(s)

    while len(s)>1:
        tmp = help(s[0], s[1])
        s.pop(0)
        s.pop(0)
        s.insert(0, tmp)
    res = s[0]
    return res


def help(s1, s2):
    n = len(s1)
    m = len(s2)
    res = []
    for i in s1:
        for j in s2:
            res.append(i + j)
    return res

digits='234'
letterCombinations(digits)