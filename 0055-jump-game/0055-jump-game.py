class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        mx = 0
        for i in range(len(nums)):
            if mx >= len(nums) - 1:
                return True
            elif nums[mx] == 0 and mx == i:
                return False

            mx = max(mx, i + nums[i])

        return True