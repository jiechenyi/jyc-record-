"""
73.矩阵置零

给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
"""

# 使用额外的空间来存储行列
def setZeroes(matrix):

    row =[] #记录0所在的行
    col =[] # 记录0所在的列

    m = len(matrix)
    n = len(matrix[0])
    for j in range(n):
        for i in range(m):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)
    for j in range(n):
        for i in range(m):
            if j in col or i in row:
                matrix[i][j] = 0
    return matrix

matrix= [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

print(setZeroes(matrix))


# 空间复杂度为O(1)

def setZeroes2(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                for k in range(n):
                    if matrix[i][k] != 0:
                        matrix[i][k] =-99999
                for l in range(m):
                    if matrix[l][j] != 0:
                        matrix[l][j] = -99999
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == -99999:
                matrix[i][j] = 0
    return matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

print(setZeroes2(matrix))






