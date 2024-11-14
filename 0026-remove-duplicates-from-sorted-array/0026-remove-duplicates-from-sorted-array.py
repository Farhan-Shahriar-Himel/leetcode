class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[k] = nums[i]
                k += 1
        nums[k] = nums[-1]
        k += 1
        return k

