class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            if len(res) >= 2:
                if s[i] == res[-1] == res[-2]:
                    continue
            res += s[i]
        
        return res