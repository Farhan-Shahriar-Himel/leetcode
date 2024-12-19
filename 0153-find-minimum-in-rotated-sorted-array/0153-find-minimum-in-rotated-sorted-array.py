class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0; right = n - 1
        ans = 1e9 + 7
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[right]:
                ans = min(ans, nums[mid])
                right = mid - 1
            else:
                left = mid + 1
        return ans