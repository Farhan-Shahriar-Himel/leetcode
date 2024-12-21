from collections import defaultdict as dd

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        adj = dd(list)
        res = [0]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(src):
            visited.add(src)
            tot = values[src]
            for child in adj[src]:
                if child not in visited:
                    tot += dfs(child)
            
            if tot % k == 0:
                res[0] += 1
                return 0
            else:
                return tot
        
        dfs(0)

        return res[0]