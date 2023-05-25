class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if obstacleGrid == [[0]]:
            return(1)
        if obstacleGrid[0][0] == 1:
            return(0)
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 0:
                obstacleGrid[0][i] = 1
            else:
                obstacleGrid[0][i] = 0
                for j in range(i,m):
                    obstacleGrid[0][j] = 0
                break
        for i in range(1,len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = 0
                for j in range(i,n):
                    obstacleGrid[j][0] = 0
                break
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        return(obstacleGrid[-1][-1])