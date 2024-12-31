class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = dict()

        def LIS(idx):            
            if idx in dp:
                return dp[idx]
            mx = 0
            for i in range(idx + 1, n):
                if nums[i] > nums[idx]:
                    mx = max(mx, LIS(i))
            
            dp[idx] = mx + 1
            return dp[idx]
        
        res = 0
        for i in range(n):
            res = max(res, LIS(i))
        
        return res
