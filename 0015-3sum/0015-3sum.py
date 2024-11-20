class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):

            l, r = i + 1, n - 1
            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                if tot == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[i] != nums[i - 1] and l < r:
                        l += 1
                elif tot > 0:
                    r -= 1
                else:
                    l += 1
        
        return res