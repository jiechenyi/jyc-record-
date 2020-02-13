"""
67.二进制求和
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。
"""

# 本人写的狗血 code

def addBinary( a, b):
    res=[]
    a = list(a)
    b = list(b)
    flag = 0
    while a and b:
        if a[-1]=='1' and b[-1] =='1' :
            a.pop(-1)
            b.pop(-1)
            if flag == 1:
                res.insert(0,"1")
                flag = 1
            else:
                res.insert(0,"0")
                flag = 1
        elif a[-1] == '0' and b[-1] == '0' :
            a.pop(-1)
            b.pop(-1)
            if flag ==1:
                res.insert(0,'1')
                flag = 0
            else :
                res.insert(0, '0')
        else:
            a.pop(-1)
            b.pop(-1)
            if flag == 1:
                res.insert(0,'0')
            else:
                res.insert(0, '1')
    while a:
        if a[-1] == "1":
            a.pop(-1)
            if flag == 1:
                res.insert(0, '0')
                flag =1
            else:
                res.insert(0, '1')
                flag = 0
        else:
            a.pop(-1)
            if flag == 1:
                res.insert(0, '1')
                flag = 0
            else:
                res.insert(0, '0')
                flag =0
    while b :
        if b[-1] == "1":
            b.pop(-1)
            if flag == 1:
                res.insert(0, '0')
                flag =1
            else:
                res.insert(0, '1')
                flag = 0
        else:
            b.pop(-1)
            if flag == 1:
                res.insert(0, '1')
                flag = 0
            else:
                res.insert(0, '0')
                flag =0
    if flag == 1:
        res.insert(0,"1")
    return ''.join(res)

a="100"
b="110010"

print(addBinary(a,b))


# 漂亮的

def addBinary2(a,b):
    res =""
    carry = 0
    val = 0

    for i in range(max(len(a),len(b))):
        val = carry
        if i <len(a):
            val += int(a[-(i+1)])
        if i < len(b):
            val += int(b[-(i+1)])
        carry = val // 2
        val = val%2

        res += str(val)
    if carry:
        res+=str(1)
    return res[::-1]





