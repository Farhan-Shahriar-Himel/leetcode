class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, posDiag, negDiag = set(), set(), set()

        res = [0]
        def backtrack(r):
            if r == n:
               res[0] += 1
            else:
                for c in range(n):
                    if c in cols or r - c in negDiag or r + c in posDiag:
                        continue
                    cols.add(c)
                    negDiag.add(r - c)
                    posDiag.add(r + c)
                    backtrack(r + 1)
                    cols.remove(c)
                    negDiag.remove(r - c)
                    posDiag.remove(r + c)
        
        backtrack(0)

        return res[0]