class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n, freq = len(nums), defaultdict(int)

        for i in range(n):
            for j in range(i + 1, n):
                freq[nums[i] * nums[j]] += 1
        
        res = 0
        for mul, cnt in freq.items():
            if cnt > 1:
                res += (cnt * (cnt - 1)) // 2
        
        return res * 8