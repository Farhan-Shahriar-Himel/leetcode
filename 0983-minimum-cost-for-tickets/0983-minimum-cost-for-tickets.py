class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = dict() 
        
        def FindCost(idx):

            if idx >= len(days):
                return 0
            
            if idx in dp:
                return dp[idx]

            oneDay = FindCost(idx + 1) + costs[0]
            weekly = FindCost(bisect_left(days, days[idx] + 7)) + costs[1]
            monthly = FindCost(bisect_left(days, days[idx] + 30)) + costs[2]

            dp[idx] = min(oneDay, weekly, monthly)
            return dp[idx]
    
        return FindCost(0)
