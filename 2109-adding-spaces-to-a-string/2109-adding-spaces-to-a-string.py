from collections import defaultdict as dd

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        mp = dd(bool)
        for el in spaces:
            mp[el] = True
        
        res = ""
        for i, ch in enumerate(s):
            if mp[i]:
                res += " "
            res += ch
        
        return res