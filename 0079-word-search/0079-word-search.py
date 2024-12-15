class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        paths = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(board)
        m = len(board[0])
        visit = set()
        
        def valid(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j, indx):
            if indx == len(word):
                return True
            visit.add((i, j))
            for dx, dy in paths:
                x = i + dx
                y = j + dy
                if valid(x, y) and not (x, y) in visit and board[x][y] == word[indx]:
                    if dfs(x, y, indx + 1):
                        return True
            visit.remove((i, j))
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visit = set()
                    if dfs(i, j, 1):
                        return True
        
        return False

