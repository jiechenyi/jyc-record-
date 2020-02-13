"""
63.不同路径

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？


"""


def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """

    m,n = len(obstacleGrid), len(obstacleGrid[0])

    dp= [[0]*n for _ in range(m)]

    if obstacleGrid == [[0]]:
        return 1

    for i in range(1,m):
        if obstacleGrid[i-1][0] == 0 and obstacleGrid[i][0] == 0:
            dp[i][0] = 1
        else:
            break
    for j in range(1,n):
        if obstacleGrid[0][j-1] == 0 and obstacleGrid[0][j] == 0:
            dp[0][j] = 1
        else:
            break

    for i in range(1,m):
        for j in range(1,n):
            if obstacleGrid[i][j] != 1:
                if obstacleGrid[i-1][j] == 0 :
                    dp[i][j] += dp[i-1][j]
                if obstacleGrid[i][j-1] == 0:
                    dp[i][j] +=  dp[i][j-1]

    return dp[-1][-1]



o = [[0,1]
]

print(uniquePathsWithObstacles(o))