class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        dir4 = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(grid)

        def valid(i, j):
            return 0 <= i < n and 0 <= j < n

        visit = set()
        dp = dict()

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            visit.add((i, j))
            child = 1
            for dx, dy in dir4:
                x = dx + i
                y = dy + j
                if not valid(x, y) or (x, y) in visit or grid[x][y] == 0:
                    continue
                child += dfs(x, y)
            
            if grid[i][j] != 0:
                dp[(i, j)] = child
            
            return child
        
        res = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    res = max(res, dfs(i, j))
                    visit = set()
        
        return res if res != -1 else n * n
                
            

