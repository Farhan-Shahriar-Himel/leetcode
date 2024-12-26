class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        left, right = 1, x
        while right - left > 1:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                left = mid
            else:
                right = mid - 1
            
        return left