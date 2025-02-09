class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n, good = len(nums), 0
        diff = dict()
        for i, num in enumerate(nums):
            d = i - num
            if d in diff:
                good += diff[d]
                diff[d] += 1
            else: 
                diff[d] = 1
        
        return ((n * (n - 1)) // 2) - good