class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = dict()

        def totalWays(i, j):
            if obstacleGrid[i][j] == 1:
                return 0

            if i == n - 1 and j == m - 1:
                return 1
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            ways = 0
            if i + 1 < n:
                ways += totalWays(i + 1, j)
            if j + 1 < m:
                ways += totalWays(i, j + 1)

            dp[(i, j)] = ways
            return dp[(i, j)]
        
        return totalWays(0, 0)