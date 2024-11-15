class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        vis = None
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] and nums[i] != vis:
                nums[k] = nums[i]
                k += 1
                vis = nums[i]
            elif nums[i] != nums[i + 1]:
                nums[k] = nums[i]
                k += 1
        
        nums[k] = nums[-1]
        return k + 1