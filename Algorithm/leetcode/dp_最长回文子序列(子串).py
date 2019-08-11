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
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=1
        
        for j in range(n):
            for i in range(j-1,-1,-1):
                if j-i+1==2 and s[i]==s[j]:
                    dp[i][j] =1
                if j-i+1>2:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
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
    dp= [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for j in range(n):
        for i in range(j-1,-1,-1):
            if s[i] == s[j]:
                dp[i][j] = max(dp[i+1][j-1]+2,dp[i+1][j],dp[i][j-1])

    