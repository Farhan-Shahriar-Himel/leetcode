class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
        
        odd = 0
        for key, value in freq.items():
            if value % 2 == 1:
                odd += 1
        
        return k >= odd and k <= len(s)
