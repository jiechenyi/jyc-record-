"""
91.解码方法

一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

"""

def numDecodings(s):
    if not s :
        return 0
    if len(s) == 1:
        if s[0] != "0":
            return 1
        else:
            return 0


    n = len(s)

    dp=[0]*(n)
    if s[0] =="0":
        return 0
    if s[1] == "0" :
        if s[0] == "1" or s[0] == "2":
            dp[0] = 1
            dp[1] = 1
        else:
            return 0

    elif int(s[0]+s[1]) <=26:
        dp[0] = 1
        dp[1] = 2
    else:
        dp[0] = 1
        dp[1] = 1

    for i in range(2,n):
        if s[i] == "0":
            if s[i-1] == "1" or s[i-1] == "2":
                dp[i] = dp[i-2]
            else:
                return 0
        else:
            if s[i-1] == "1" or (s[i-1] == "2" and "1"<=s[i]<='6'):
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
    return dp[-1]

s="110"
print(numDecodings(s))