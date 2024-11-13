class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for pairs in intervals:
            if len(ans) == 0:
                ans.append(pairs)
            elif ans[-1][1] >= pairs[0]:
                ans[-1][1] = max(ans[-1][1], pairs[1])
            else:
                ans.append(pairs)
        return ans