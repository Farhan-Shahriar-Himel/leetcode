class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, res = 0, 1
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                res = max(res, i - l + 1)
            else:
                l = i
        
        l = 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                res = max(res, i - l + 1)
            else:
                l = i
        
        return res