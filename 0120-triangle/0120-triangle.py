class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        heap = [(triangle[0][0], 0, 0)]
        dist = defaultdict(lambda: float('inf'))
        dist[(0, 0)] = triangle[0][0]

        while heap:
            w, i, j = heappop(heap)

            if w > dist[(i, j)]: continue

            for idx in range(2):
                x = i + 1
                y = j + idx
                
                if x < n and dist[(x, y)] > dist[(i, j)] + triangle[x][y]:
                    dist[(x, y)] = dist[(i, j)] + triangle[x][y]
                    heappush(heap, (dist[(x, y)], x, y))

        res = float('inf')
        for i in range(len(triangle[-1])):
            res = min(res, dist[(n - 1, i)])
        
        return res


        
