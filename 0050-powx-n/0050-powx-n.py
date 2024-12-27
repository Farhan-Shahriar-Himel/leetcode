class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = power(x, n // 2)
            res *= res
            return res if n % 2 == 0 else res * x
        
        res = power(x, abs(n))
        return res if n >= 0 else 1 / res
        
            
        