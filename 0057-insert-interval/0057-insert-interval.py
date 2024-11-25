class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []
        for pair in intervals:
            if len(res) == 0:
                res.append(pair)
            elif res[-1][1] >= pair[0]:
                res[-1][1] = max(res[-1][1], pair[1])
            else:
                res.append(pair)
        
        return res