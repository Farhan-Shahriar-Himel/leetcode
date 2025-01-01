class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = dict()
        def Solve(i, j):
            if i >= len(triangle):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]

            op1 = Solve(i + 1, j) + triangle[i][j]
            op2 = Solve(i + 1, j + 1) + triangle[i][j]

            dp[(i, j)] = min(op1, op2)
            return dp[(i, j)]
        
        return Solve(0, 0)
            
            


        
