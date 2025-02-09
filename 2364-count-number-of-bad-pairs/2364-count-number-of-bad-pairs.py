class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n, good = len(nums), 0
        diff = defaultdict(int)
        for i in range(n):
            diff[i - nums[i]] += 1
        
        for k, v in diff.items():
            good += (v * (v - 1)) // 2
        
        return ((n * (n - 1)) // 2) - good