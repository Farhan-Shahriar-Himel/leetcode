class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n, m = len(s), len(part)
        while part in s:
            s = s.replace(part, "", 1)
        return s

