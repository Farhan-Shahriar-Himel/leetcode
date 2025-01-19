class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n, m = len(heightMap), len(heightMap[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def isValid(i, j):
            return 0 <= i < n and 0 <= j < m
        
        heap, visit = [], set()

        for i in range(n):
            heappush(heap, (heightMap[i][0], i, 0))
            visit.add((i, 0))
            heappush(heap, (heightMap[i][m - 1], i, m - 1))
            visit.add((i, m - 1))

        for i in range(m):
            heappush(heap, (heightMap[0][i], 0, i))
            visit.add((0, i))
            heappush(heap, (heightMap[n - 1][i], n - 1, i))
            visit.add((n - 1, i))

        level, water = 0, 0
        while heap:
            height, i, j = heappop(heap)
            level = max(level, height)
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if not isValid(x, y) or (x, y) in visit: continue
                heappush(heap, (heightMap[x][y], x, y))
                visit.add((x, y))
                if heightMap[x][y] < level:
                    water += level - heightMap[x][y]
        
        return water
