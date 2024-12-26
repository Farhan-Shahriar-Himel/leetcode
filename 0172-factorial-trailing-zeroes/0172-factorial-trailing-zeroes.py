class Solution:
    def trailingZeroes(self, n: int) -> int:
        res, pwr = 0, 1
        deno = 5
        while n >= deno:
            res += n // deno
            deno *= 5
        
        return res