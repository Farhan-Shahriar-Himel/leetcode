class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums = dict()
        for key, val in nums1:
            nums[key] = val
        
        for key, val in nums2:
            nums[key] = nums.get(key, 0) + val
        
        res = []
        for i in range(1, 1001):
            if i in nums:
                res.append([i, nums[i]])

        return res 