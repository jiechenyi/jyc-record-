"""
最长回文子串

"""
def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:
            return ""
        n = len(s)
        dp = [[0]*n for _ in range(n)] # 记录 dp[i][j] ,i～j 是否是回文的，是的话标为1，否则标为0
        for i in range(n):
            dp[i][i]=1
        
        for j in range(n):
            for i in range(j-1,-1,-1):
                if j-i+1==2 and s[i]==s[j]: # 如果dp[i][j]，i和j是相邻
                    dp[i][j] =1
                if j-i+1>2:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] # 左右都往里面缩一个字符
                    else:
                        dp[i][j] = 0
        res =-99
        for i in range(n):
            for j in range(i,n):
                if dp[i][j] == 1 and j-i > res:
                    left =i
                    right =j
                    res = j-i
        return s[left:right+1]
                    
"""
最长回文子序列的长度
"""
def f(s):
    if not s:
        return ""
    n = len(s)
    dp= [[0]*n for _ in range(n)] # 记录的是i～j 之间的 回文序列的长度
    for i in range(n):
        dp[i][i] = 1
    for j in range(n):
        for i in range(j-1,-1,-1):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]+2
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])
    return dp[0][-1]