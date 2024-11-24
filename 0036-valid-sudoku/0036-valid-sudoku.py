from collections import defaultdict as dd

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        bx = dd(set)
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j] in row:
                    return False
                elif board[j][i] in col:
                    print(j, i, board[j][i], col)
                    return False
                elif board[i][j] in bx[(i//3, j//3)]:
                    return False
                if board[i][j] != '.': row.add(board[i][j])
                if board[j][i] != '.': col.add(board[j][i])
                if board[i][j] != '.': bx[(i//3, j//3)].add(board[i][j])

        return True