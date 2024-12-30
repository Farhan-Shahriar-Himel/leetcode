class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = dict()
        def makeAmount(tot):
            if tot == amount:
                return 0
            if tot > amount:
                return float('inf')
            
            if tot in dp:
                return dp[tot]

            need = float('inf')
            for coin in coins:
                if tot + coin <= amount:
                    need = min(need, makeAmount(tot + coin))
            
            dp[tot] = need + 1
            return dp[tot]
        
        res = makeAmount(0) 

        return res if res != float('inf') else -1