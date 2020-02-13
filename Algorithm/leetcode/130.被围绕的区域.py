"""
130.被围绕的区域
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

"""

# DFS
def solve(board):

    if not board or not board[0]:
        return
    m = len(board)
    n = len(board[0])

    def dfs(i,j):
        board[i][j] ="B"
        for x, y in [(-1,0),(1,0), (0,-1),(0,1)]:
            tmp_i = i+x

            tmp_j = j+y

            if 1<= tmp_i < m and 1<= tmp_j < n and board[tmp_i][tmp_j] == "O":
                dfs(tmp_i, tmp_j)
    for i in range(m):
        if board[i][0] =="O":
            dfs(i,0)

        if board[i][n-1] == "O":
            dfs(i,n-1)
    for j in range(n):
        if board[0][j] == "O":
            dfs(0,j)
        if board[m-1][j] == "O":
            dfs(m-1, j)
    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                board[i][j] = "X"

            if board[i][j] =="B":
                board[i][j] = "O"

# BFS


