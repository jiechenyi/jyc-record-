"""

48.旋转图像
将矩阵顺时针旋转90度

"""

n = len(matrix)
for i in range(n):
    for j in range(n):
        if i < j:
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
for i in range(n):
    matrix[i] = matrix[i][::-1]
print(matrix)


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """





matrix =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

rotate(matrix)