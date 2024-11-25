from collections import defaultdict as dd

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dd(list)
        for i, wrd in enumerate(strs):
            wrd = tuple(sorted(wrd))
            d[wrd].append(i)
        
        res = []
        for lst in d.values():
            group = []
            for i in lst:
                group.append(strs[i])
            res.append(group)
        
        return res