class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        paths = [(1, 0), (-1, 0), (0, 1), (0, - 1)]

        n = len(board)
        m = len(board[0])
        vis = [[False] * m for _ in range(n)]

        def Valid(i, j):
            return i >= 0 and i < n and j >= 0 and j < m
        
        def dfs(i, j, do):
            if do:
                board[i][j] = 'X'
            vis[i][j] = True
            for dx, dy in paths:
                x = i + dx
                y = j + dy
                if Valid(x, y) and board[x][y] == 'O' and not vis[x][y]:
                    dfs(x, y, do)
        
        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0, False)
            if board[i][m - 1] == 'O':
                dfs(i, m - 1, False)
        
        for i in range(m):
            if board[0][i] == 'O':
                dfs(0, i, False)
            if board[n - 1][i] == 'O':
                dfs(n - 1, i, False)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not vis[i][j]:
                    dfs(i, j, True)
