class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if len(newInterval) == 0:
            return intervals

        n = len(intervals)
        res = []
        i = 0
        while i < n:
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                break
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        res.append(newInterval)

        for x in range(i, n):
            res.append(intervals[x])

        return res
            