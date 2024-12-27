class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = dict()

        def climbCount(n):

            if n in dp:
                return dp[n]

            if n == 0:
                return 1
            if n < 0:
                return 0
            
            pos1 = climbCount(n - 1)
            pos2 = climbCount(n - 2)

            dp[n] = pos1 + pos2
            return dp[n]
        
        return climbCount(n)



