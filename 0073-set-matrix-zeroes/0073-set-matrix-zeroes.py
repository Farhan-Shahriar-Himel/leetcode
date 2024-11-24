class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        row = {}
        col = {}
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True


        for i in range(n):
            for j in range(m):
                if i in row or j in col:
                    matrix[i][j] = 0
               