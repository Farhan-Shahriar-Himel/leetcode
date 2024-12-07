from collections import defaultdict as dd, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = dd(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            q, vis = deque(), set()
            q.append((src, 1))
            vis.add(src)
            while q:
                var, val = q.popleft()
                if var == target:
                    return val
                for child, wt in adj[var]:
                    if child not in vis:
                        q.append((child, wt * val))
                        vis.add(child)
            return -1

        return [bfs(a, b) for a, b in queries]