

"""

72.编辑距离
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

"""

def minDistance(word1,word2):
    if not word1:
        return len(word2)
    if not word2:
        return len(word2)

    n = len(word1)
    m = len(word2)

    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for j in range(m+1):
        dp[0][j] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1] + 1,dp[i][j-1] +1 ,dp[i-1][j]+1)
    return dp[-1][-1]
