class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        if not nums:
            return [-1, -1]
        
        first = -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        if nums[l] == target:
            first = l
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        
        if nums[r - 1] == target:
            return [first, r - 1]
        
        return [-1, -1]