class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n, good = len(nums), 0
        diff = defaultdict(int)
        for i, num in enumerate(nums):
            good += diff[i - num]
            diff[i - num] += 1
        
        return ((n * (n - 1)) // 2) - good