from heapq import heappush as push, heappop as pop


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def valid(x, y):
            return x >= 0 and x < n and y >= 0 and y < m

        paths = [
            [1, 0], [-1, 0], [0, 1], [0, -1]
        ]
        dist = [[float('inf') for i in range(m)] for i in range(n)]
    
        pq = []
        dist[0][0] = 0
        push(pq, [dist[0][0], 0, 0])
        while pq:
            par = pop(pq)
            wt = par[0]
            si, sj = par[1], par[2]
            if wt > dist[si][sj]: continue
            for path in paths:
                i = si + path[0]
                j = sj + path[1]
                if not valid(i, j): continue
                w = grid[i][j]
                if dist[si][sj] + w < dist[i][j]:
                    dist[i][j] = dist[si][sj] + w
                    push(pq, [dist[i][j], i, j])
        
        return dist[n - 1][m - 1]
