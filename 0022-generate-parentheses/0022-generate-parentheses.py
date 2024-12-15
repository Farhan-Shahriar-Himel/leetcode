class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def makeComb(opening, closing, s):
            if opening == closing and len(s) == n * 2:
                res.append(s)
                return
            
            if opening < n:
                makeComb(opening + 1, closing, s + '(')

            if closing < opening:
                makeComb(opening, closing + 1, s + ')')
        
        makeComb(0, 0, "")

        return res