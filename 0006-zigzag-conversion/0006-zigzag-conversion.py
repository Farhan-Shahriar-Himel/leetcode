class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        inc = 2 * (numRows - 1)
        res = ""
        for r in range(numRows):
            for i in range(r, len(s), inc):
                res += s[i]
                if r > 0 and r < numRows - 1:
                    ind = i + inc - 2 * r
                    if ind < len(s):
                        res += s[ind]
        
        return res