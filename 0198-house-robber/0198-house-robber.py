class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = dict()
        
        def maxRobbed(idx):

            if idx in dp:
                return dp[idx]

            if idx >= len(nums):
                return 0
            
            pos1 = maxRobbed(idx + 2) + nums[idx]
            pos2 = maxRobbed(idx + 3) + nums[idx]

            dp[idx] = max(pos1, pos2)
            return dp[idx]
        
        return max(maxRobbed(0), maxRobbed(1))