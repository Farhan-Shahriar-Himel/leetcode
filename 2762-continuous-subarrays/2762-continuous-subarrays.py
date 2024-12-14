class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = res = 0
        mx, mn = float(-inf), float(inf)

        while r < n:
            mx = max(mx, nums[r])
            mn = min(mn, nums[r])

            if abs(mx - mn) > 2:
                window = r - l
                res += (window * (window + 1)) // 2
                l = r
                mx = nums[r]
                mn = nums[r]
                while abs(nums[r] - nums[l - 1]) <= 2:
                    l -= 1
                    mx = max(mx, nums[l])
                    mn = min(mn, nums[l])

                if l < r:
                    window = r - l
                    res -= (window * (window + 1)) // 2
            
            r += 1
        
        window = r - l
        res += (window * (window + 1)) // 2

        return res
            