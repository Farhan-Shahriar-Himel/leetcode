class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def isPossible(x):
            i = robbed = 0
            while i < n:
                if nums[i] <= x:
                    robbed += 1
                    i += 2
                else:
                    i += 1
            return robbed >= k


        l, r = 1, max(nums)
        while l <= r:
            mid = l + (r - l) // 2
            if isPossible(mid):
                r = mid - 1
            else:
                l = mid + 1
            
        return l

