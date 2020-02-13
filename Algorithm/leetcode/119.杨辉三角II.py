"""
119.杨辉三角

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
"""

def getRow(rowIndex):

    if rowIndex==1:
        return [1]
    if rowIndex== 2:
        return [1,1]

    dp =[[1],[1,1]]
    i=1
    while i<rowIndex:
        n = len(dp[-1])+1
        tmp = [0]*n
        tmp[0] = 1
        tmp[-1] = 1
        for i in range(1,n-1):
            tmp[i] = dp[-1][i-1]+dp[-1][i]
        dp.append(tmp)
        i +=1
    return dp[-1]

k = 3
print(getRow(k))