class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyed = None
        profit = 0
        i = 0
        for i in range(len(prices)):
            if i == len(prices) - 1:
                if buyed:
                    profit += prices[i] - buyed
            elif prices[i] > prices[i + 1] and buyed:
                profit += prices[i] - buyed
                buyed = None
            elif prices[i] < prices[i + 1] and not buyed:
                buyed = prices[i]

        return profit