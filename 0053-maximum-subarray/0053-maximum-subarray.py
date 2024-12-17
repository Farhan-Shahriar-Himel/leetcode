class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = tot = -float('inf')
        for num in nums:
            tot = max(num, tot + num)
            res = max(res, tot)
        return res