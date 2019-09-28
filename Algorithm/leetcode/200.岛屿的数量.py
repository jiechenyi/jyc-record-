"""

200.岛屿的数量

"""


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    n = len(grid)
    m = len(grid[0])
    stack=[]

    for k in range(n):
        for l in range(m):
            while stack:
                i, j = stack.pop()
                if i - 1 >= 0 and grid[i - 1][j] == "1":
                    stack.append((i - 1, j))
                    grid[i-1][j] = 2
                if j + 1 < m and grid[i][j + 1] == "1":
                    stack.append((i, j + 1))
                    grid[i][j+1] =2
                if i + 1 < n and grid[i + 1][j] == "1":
                    stack.append((i + 1, j))
                    grid[i+1][j] =2
                if j - 1 >= 0 and grid[i][j - 1] == "1":
                    stack.append((i, j - 1))
                    grid[i][j-1] = 2
            if grid[k][l] =="1":
                start =[k,l]
                stack.append(start)
                grid[k][l] = 9



    print(grid)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 9:
                cnt +=1
    return cnt



grid =[["1","1","1","1","1"],["1","0","1","0","1"],["1","1","1","1","1"]]
print(numIslands(grid))
