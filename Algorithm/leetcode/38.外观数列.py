'''

38.外观数列
整数列从1开始每一项都是对前一项描述
1. 1
2. 11
3. 21
4. 1211
5. 111221
...


'''





def split(s):
    tmp=''
    res =''

    n = len(s)
    i = 1
    tmp += s[0]
    while i<n:
        if tmp[0] == s[i] :
            tmp +=s[i]

        else:
            res += str(len(tmp))+tmp[0]
            tmp = s[i]
        i +=1
    res +=  str(len(tmp))+tmp[0]
    return res

# print(split("1221112"))

def countAndSay( n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return "1"
    if n ==2:
        return "11"
    return split(countAndSay(n-1))

print(countAndSay(6))

