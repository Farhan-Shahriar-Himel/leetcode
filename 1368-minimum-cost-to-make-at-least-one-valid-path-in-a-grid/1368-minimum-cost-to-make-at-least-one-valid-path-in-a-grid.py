class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        direction = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(grid), len(grid[0])

        def Valid(i, j):
            return i >= 0 and i < n and j >= 0 and j < m

        def dijkstra():
            q = [(0, 0, 0)]
            dist = defaultdict(lambda: float('inf'))
            dist[(0, 0)] = 0
            while q:
                cost, i, j = heappop(q)
                
                if (i == n - 1 and j == m - 1): return cost

                for dx, dy in direction[1:]:
                    x = i + dx
                    y = j + dy
                    tCst = cost
                    if (dx, dy) != direction[grid[i][j]]:
                        tCst += 1

                    if not Valid(x, y): continue

                    if dist[(x, y)] > tCst:
                        dist[(x, y)] = tCst
                        heappush(q, (dist[(x, y)], x, y))
            
            return dist[(n - 1, m - 1)]

        

        return dijkstra()