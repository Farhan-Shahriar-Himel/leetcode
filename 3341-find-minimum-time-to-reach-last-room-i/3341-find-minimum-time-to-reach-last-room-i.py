class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        directions = [
            [0, 1], [1, 0], [0, -1], [-1, 0]
        ]

        n = len(moveTime)
        m = len(moveTime[0])

        def isValid(i, j):
            return 0 <= i < n and 0 <= j < m

        def dijkstra():
            heap = []
            heapq.heappush(heap, [0, 0, 0])
            time_map = [[float('inf')] * m for _ in range(n)]
            time_map[0][0] = 0
            while heap:
                i, j, t = heapq.heappop(heap)

                if t > time_map[i][j]:
                    continue
                
                if (i, j) == (n - 1, m - 1):
                    return t

                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
    
                    if not isValid(x, y):
                        continue
                    
                    wt = max(t, moveTime[x][y]) + 1

                    if wt < time_map[x][y]:
                        time_map[x][y] = wt
                        heapq.heappush(heap, [x, y, wt])
            
            return -1
            
        return dijkstra()

                    