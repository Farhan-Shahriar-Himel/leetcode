class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(limit + 1):
            if n - i <= limit * 2:
                res += min(n - i, limit) - max(0, n - i - limit) + 1
        return res