class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = curr_mx = curr_mn = 0
        mx_sm, mn_sm = -float(inf), float(inf)
        for num in nums:
            total += num
            curr_mx = max(num, curr_mx + num)
            curr_mn = min(num, curr_mn + num)
            mx_sm = max(curr_mx, mx_sm)
            mn_sm = min(curr_mn, mn_sm)
        
        return mx_sm if curr_mn == total else max(mx_sm, total - mn_sm)
        