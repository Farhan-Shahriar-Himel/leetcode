from collections import defaultdict as dd

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def makeAdj(edges):
            adj = dd(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj
        
        adj1 = makeAdj(edges1)
        adj2 = makeAdj(edges2)
        
        def dfs(root, par, adj):
            mx_d, deapth = 0, [0, 0]
            for child in adj[root]:
                if child != par:
                    dia, dpth = dfs(child, root, adj)
                    deapth.append(dpth)
                    mx_d = max(mx_d, dia)
            
            deapth.sort()
            mx_d = max(mx_d, deapth[-1] + deapth[-2])
            return [mx_d, deapth[-1] + 1]
   
        
        d1, _ = dfs(0, -1, adj1)
        d2, _ = dfs(0, -1, adj2)

        return max(d1, d2, ((d1 + 1) // 2) + 1 + ((d2 + 1) // 2))
