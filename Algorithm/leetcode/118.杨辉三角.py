"""
118.杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""

def generate(numRows):

    if numRows==1:
        return [[1]]
    if numRows == 2:
        return [[1],[1,1]]

    res =[[1],[1,1]]
    while len(res)<numRows:
        n = len(res[-1])+1
        tmp = [0]*n
        tmp[0] = 1
        tmp[-1] = 1
        for i in range(1,n-1):
            tmp[i] = res[-1][i-1]+res[-1][i]
        res.append(tmp)
    return res

numRow = 5

print(generate(numRow))


