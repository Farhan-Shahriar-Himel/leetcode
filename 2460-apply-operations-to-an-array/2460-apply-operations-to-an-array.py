class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        zeros, numbers = [], []
        for num in nums:
            if num == 0:
                zeros.append(num)
            else:
                numbers.append(num)
        
        return numbers + zeros