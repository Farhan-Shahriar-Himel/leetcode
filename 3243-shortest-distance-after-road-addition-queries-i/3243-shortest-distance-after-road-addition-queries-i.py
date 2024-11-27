from collections import deque

class Solution:
    def __init__(self):
        self.adj = [[] for i in range(507)]


    def bfs(self, src, n):
        dist = [0] * (n + 7)
        vis = [False] * (n + 7)
        q = deque()
        q.append(src)
        while q:
            par = q.popleft()
            for child in self.adj[par]:
                if vis[child]: continue
                vis[child] = True
                q.append(child)
                dist[child] = dist[par] + 1
        
        return dist[n - 1]


    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        res = []
        
        for i in range(n - 1):
            self.adj[i].append(i + 1)

        for u, v in queries:
            self.adj[u].append(v)
            res.append(self.bfs(0, n))
        
        return res
