class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n, res = len(prices), []
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    res.append(prices[i] - prices[j])
                    break
            else:
                res.append(prices[i])
        return res