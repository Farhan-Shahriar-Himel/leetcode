class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n, m = len(s), len(part)
        while part in s:
            i = s.find(part)
            s = s[:i] + s[i + m:]
        return s

