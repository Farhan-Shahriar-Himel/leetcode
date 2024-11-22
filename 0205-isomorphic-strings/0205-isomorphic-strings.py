class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                return False

        d = {}
        for i in range(len(t)):
            if t[i] not in d:
                d[t[i]] = s[i]
            elif d[t[i]] != s[i]:
                return False

        return True