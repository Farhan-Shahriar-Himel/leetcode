class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visit = set()

        def valid(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j):
            visit.add((i, j))
            tot = grid[i][j]
            for dx, dy in directions:
                x = dx + i
                y = dy + j
                if not valid(x, y) or grid[x][y] == 0 or (x, y) in visit:
                    continue
                tot += dfs(x, y)
            
            return tot
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 or (i, j) in visit:
                    continue
                res = max(res, dfs(i, j))
        
        return res
                