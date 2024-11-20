class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if target in nums:
            return 1

        n = len(nums)
        i, j = 0, 0
        value = 0
        res = int(1e9 + 7)
        ok = False
        while i < n:
            while j < n and value < target:
                value += nums[j]
                j += 1
            if value >= target:
                res = min(res, j - i)
                ok = True
            
            value -= nums[i]
            i += 1

        return res if ok else 0