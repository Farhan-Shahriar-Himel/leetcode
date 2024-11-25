class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new = sorted(nums)
        n = len(nums)
        i, j = 0, n - 1
        ans = []
        while i < j:
            value = new[i] + new[j]
            if value == target:
                ans = [new[i], new[j]]
                break
            elif value < target:
                i += 1
            else:
                j -= 1
        
        x = nums.index(ans[0])
        for i in range(n):
            if i != x and nums[i] == ans[1]:
                return [x, i]
        
        return [-1, -1]
            