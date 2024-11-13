class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tot = 0
        ans = -(1e9 + 7)
        for el in nums:
            tot += el
            ans = max(tot, ans)
            if tot < 0:
                tot = 0
        return ans