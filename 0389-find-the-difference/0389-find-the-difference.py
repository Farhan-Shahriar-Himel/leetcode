from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        while len(s) != 0:
            if s[-1] == t[-1]:
                s.pop()
                t.pop()
            else:
                return t[-1]
        
        return t[0]