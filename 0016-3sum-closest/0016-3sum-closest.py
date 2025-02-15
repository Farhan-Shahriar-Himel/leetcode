class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n, res = len(nums), float('inf')
        for i in range(0, n):
            l, r = i + 1, n - 1
            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                if abs(tot - target) <  abs(target - res):
                    res = tot
                if tot == target:
                    return target
                elif tot > target:
                    r -= 1
                else:
                    l += 1
        return res
            
            