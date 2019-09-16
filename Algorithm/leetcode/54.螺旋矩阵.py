"""
54.螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

(边界条件注意一下) 有时间的话可以看下其他解法
"""


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix:
        return
    n = len(matrix)
    m = len(matrix[0])

    res = []
    i=0
    while i <len(matrix):
        if len(matrix[i])>0:
            res.extend(matrix[i])
            matrix.pop(i)
            if len(matrix)>0:
                for k in range(len(matrix)):
                    if len(matrix[k]) >0:
                        res.append(matrix[k][-1])
                        matrix[k].pop(-1)
                res.extend(matrix[-1][::-1])
                matrix.pop(-1)
            if len(matrix)>1 :
                for m in range(len(matrix) - 1, 0, -1):
                    if len(matrix[m]) >0:
                        res.append(matrix[m][0])
                        matrix[m].pop(0)
                    else:
                        break
        else:
            break
    return res

matrix=[[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
print(spiralOrder(matrix))