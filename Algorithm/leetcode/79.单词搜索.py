"""
79.单词搜索

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



"""
# 递归 深度优先搜索（DFS）和回溯
# 在board中找到单词可能的起始位置 展开一轮搜索 这轮搜索要么失败（那么寻找下一个单词可能起始的位置） 要么成功
# 全部搜索完之后 返回最后结果
def exist(board,word):

    m = len(board)
    n = len(board[0])


    def search(i,j,d):
        if i >= m or j >= n or i<0 or j<0:
            return False
        if board[i][j] != word[d]:
            return False
        if d == len(word)-1:
            return True

        cur = board[i][j]
        board[i][j] = 0 # 对于搜索过的要做一个标记

        flag = search(i-1,j,d+1) or search(i+1,j,d+1) or search(i,j+1,d+1) or search(i, j-1,d+1) # 在上下左右递归寻找

        board[i][j] = cur # 此轮搜索结束后 要把这个标记去除 不去影响下一轮搜索

        return flag
    for i in range(m):
        for j in range(n):
            if search(i,j,0):
                return True
    return False