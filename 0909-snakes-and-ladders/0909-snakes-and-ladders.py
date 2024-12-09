from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()

        def get_indxs(sqr):
            r = (sqr - 1) // n
            c = (sqr - 1) % n
            if r & 1:
                c = n - 1 - c
            return r, c

        def bfs(src):
            q = deque()
            q.append([src, 0])
            seen = set()
            while q:
                sqr, level = q.popleft()
                for i in range(1, 7):
                    dest = sqr + i
                    r, c = get_indxs(dest)
                    if board[r][c] != -1:
                        dest = board[r][c]
                    if dest == n * n:
                        return level + 1
                    if dest not in seen:
                        q.append([dest, level + 1])
                        seen.add(dest)
            
            return -1
        
        return bfs(1)
