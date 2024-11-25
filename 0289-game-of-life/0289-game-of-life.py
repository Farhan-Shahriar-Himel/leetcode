class Solution:
    def __init__(self):
        self.paths = [
            (1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)
        ]

    def valid(self, i, j, board):
        n = len(board)
        m = len(board[0])
        return i >= 0 and i < n and j >= 0 and j < m


    def neighbour(self, i, j, board):
        live, death = 0, 0
        for x, y in self.paths:
            ni = i + x
            nj = j + y
            if self.valid(ni, nj, board):
                # print(ni, nj, board[ni][nj])
                if board[ni][nj] == 1:
                    live += 1
                else:
                    death += 1
        
        return (live, death)
        


    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        matrix = [tmp[:] for tmp in board]

        for i in range(n):
            for j in range(m):
                live, death = self.neighbour(i, j, board)
                if board[i][j] == 0:
                    if live == 3:
                        matrix[i][j] = 1
                else:
                    if live < 2 or live > 3:
                        matrix[i][j] = 0
        
        board[:] = matrix

                