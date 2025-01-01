class Solution:
    def maxScore(self, s: str) -> int:
        one = s.count('1')
        zero = res = 0
        for ch in s:
            if ch == '0':
                zero += 1
            else:
                one -= 1
            res = max(res, one + zero)
        
        return res