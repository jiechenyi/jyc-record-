"""

36.有效的数独

判断数组是否有效
"十字"上的数字都不能重复

"""


def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    if not board: return True

    n = 9
    col = [[0] * 9 for _ in range(9)]  # 记录 每一列 数字出现的次数
    row = [[0] * 9 for _ in range(9)]  # 记录每一行数字出现的次数
    block = [[0] * 9 for _ in range(9)]  # 有 9 个block
    for i in range(n):
        for j in range(n):
            if board[i][j] == ".":
                continue
            else:
                tmp = int(board[i][j])
                col[j][tmp - 1] = col[j][tmp - 1] + 1
                row[i][tmp - 1] = row[i][tmp - 1] + 1
                blockIndex = int(i / 3 * 3 + j / 3)

                block[blockIndex][tmp - 1] += 1
                if col[j][tmp - 1] >= 2:
                    return False
                if row[i][tmp - 1] >= 2:
                    return False
                if block[blockIndex][tmp - 1] >= 2:
                    return False

    return True


board=[[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]

print(isValidSudoku(board))