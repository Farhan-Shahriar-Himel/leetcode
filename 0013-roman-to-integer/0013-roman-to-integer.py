class Solution:
    def romanToInt(self, s: str) -> int:
        rank = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = int(1e3 + 7)
        value = 0
        for ch in s:
            if rank[ch] <= prev:
                value += rank[ch]
                prev = rank[ch]
            else:
                value -= 2 * prev
                value += rank[ch]
        
        return value