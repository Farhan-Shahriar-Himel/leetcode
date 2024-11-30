class Solution:
    def reverse(self, x: int) -> int:

        low = -(1 << 31)
        high = (1 << 31) - 1

        res = 0
        num = max(x, -1 * x)
        while num:
            res = res * 10 + (num % 10)
            num //= 10
        
        if res < low or res > high:
            return 0
        
        return res if x > 0 else -1 * res