class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        nums = [(values[j] - j) for j in range(n)] + [-float('inf')]

        for i in range(n - 1, -1, -1):
            nums[i] = max(nums[i], nums[i + 1])
        
        res = -float('inf')
        for i in range(n):
            res = max(res, values[i] + i + nums[i + 1])

        return res 