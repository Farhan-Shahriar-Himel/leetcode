class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n, res = len(prices), []
        for i in range(n - 1):
            mnIndx = -1
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    mnIndx = j
                    break
            if mnIndx != -1:
                res.append(prices[i] - prices[mnIndx])
            else:
                res.append(prices[i])
        res.append(prices[-1])
        return res