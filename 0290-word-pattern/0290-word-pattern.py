class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        d = {}
        
        if len(s) != len(pattern): return False

        for i in range(len(s)):
            if pattern[i] in d and d[pattern[i]] != s[i]:
                return False
            d[pattern[i]] = s[i]
        
        d = {}

        for i in range(len(s)):
            if s[i] in d and d[s[i]] != pattern[i]:
                return False
            d[s[i]] = pattern[i]

        
        return True