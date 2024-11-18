class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        n = len(s)
        wrd = []

        ok = False
        for i in range(n - 1, -1, -1):
            if s[i] != " ":
               wrd.append(s[i])
               ok = True
            else:
                if ok:
                    res.append("".join(wrd)[::-1])
                    ok = False
                wrd = []
        if len(wrd) > 0:
            res.append("".join(wrd)[::-1])

        ans = " ".join(res)
        return ans