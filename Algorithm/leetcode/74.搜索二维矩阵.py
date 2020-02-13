"""
74.搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

"""

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):

        if matrix[i][-1] < target: # 跳到下一排
            continue
        elif matrix[i][0] > target:
            return False

        left = 0
        right = n

        while left <= right:
            mid = int(left+(right-left)/2)
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                right = mid-1
            else:
                left = mid + 1
    return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13

print(searchMatrix(matrix, target))


