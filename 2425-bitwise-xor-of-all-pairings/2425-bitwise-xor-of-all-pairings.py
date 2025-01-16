class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        ans = 0
        
        def XOR(nums):
            ans = 0
            for num in nums:
                ans ^= num
            return ans
        
        res = 0
        if n % 2 == 1:
            res ^= XOR(nums2)
        if m % 2 == 1:
            res ^= XOR(nums1)

        return res 