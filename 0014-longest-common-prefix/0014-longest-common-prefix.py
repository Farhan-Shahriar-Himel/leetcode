class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mn = min(len(s) for s in strs)
        res = []
        for i in range(mn):
            ok = True
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != ch:
                    ok = False
            if ok:
                res.append(ch)
            else:
                break
        
        return "".join(res)