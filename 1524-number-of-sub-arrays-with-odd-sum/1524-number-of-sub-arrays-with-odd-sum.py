class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, prefixSum, mod, n = 0, 0, int(1e9 + 7), len(arr)
        for a in arr:
            prefixSum += a
            odd += prefixSum % 2
        odd += (n - odd) * odd
        return odd % mod