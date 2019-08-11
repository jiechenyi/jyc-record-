"""
6.将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

numrow =4
output=LDREOEIIECIHNTSG

"""

def revert(s,numrow):
    if not s:
        return ""
    tmp = [""] * numrow
    l = []
    n = len(s)
    i = 0
    j = 1
    while i < n:
        if j <= numrow:
            tmp[j - 1] = s[i]
            j += 1
            i += 1
        else:
            j=1
            l.append(tmp)
            m = numrow - 2
            k = 1
            tmp = [""] * numrow
            while m > 0 and i < n:
                tmp[numrow - 1 - k] = s[i]
                k = k+1
                m = m -1
                i += 1
                l.append(tmp)
                tmp = [""] * numrow
    l.append(tmp)
    res = ''
    m = len(l)
    for i in range(numrow):
        for j in range(m):
            res += l[j][i]
    return res


s ="PAYPALISHIRING"
numrow =5

print(revert(s,numrow))

