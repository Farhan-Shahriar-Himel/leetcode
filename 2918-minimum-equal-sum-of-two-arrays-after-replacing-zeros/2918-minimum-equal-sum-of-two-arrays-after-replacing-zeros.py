class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1, z2 = nums1.count(0), nums2.count(0)
        s1, s2 = sum(nums1), sum(nums2)

        if z1 == 0 and s2 + z2 > s1:
            return -1
        if z2 == 0 and s1 + z1 > s2:
            return -1
        
        return max(s1 + z1, s2 + z2)