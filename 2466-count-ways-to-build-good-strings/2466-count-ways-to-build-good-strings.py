class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = dict()
        def count(x):
            if x > high:
                return 0
            if x in dp:
                return dp[x]
            
            dp[x] = low <= x <= high
            dp[x] += count(x + zero) + count(x + one)
            return dp[x] % mod
        
        return count(0)