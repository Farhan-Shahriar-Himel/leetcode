class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for x in [1, -1]:
                j = i + x
                if 0 <= j < n and nums[i] % 2 == nums[j] % 2:
                    return False
        return True