class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        for x1, y1 in points:
            mp = defaultdict(int)
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                if x1 == x2:
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)
                mp[slope] += 1
                res = max(res, mp[slope] + 1)
        
        return res