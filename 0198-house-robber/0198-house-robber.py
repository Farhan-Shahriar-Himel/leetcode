class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp, n = [0] * 107, len(nums)
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        
        return max(dp[n - 1], dp[n - 2])
        