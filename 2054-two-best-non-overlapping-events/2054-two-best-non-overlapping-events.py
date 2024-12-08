class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        suffMax = [0] * n
        suffMax[-1] = events[-1][-1]
        for i in range(n - 2, -1, -1):
            suffMax[i] = max(suffMax[i + 1], events[i][-1])
        
        res = 0
        for i in range(n):
            left, right = i + 1, n - 1
            target = -1
            while left <= right:
                mid = left + (right - left) // 2
                if events[i][1] < events[mid][0]:
                    target = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if target != -1:
                res = max(res, events[i][-1] + suffMax[target])
            res = max(res, events[i][-1])
        
        return res
