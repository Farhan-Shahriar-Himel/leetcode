class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(1007)]
        rank = [0] * 1007

        def findRoot(v):
            if v == parent[v]:
                return v
            parent[v] = findRoot(parent[v])
            return parent[v]
        
        def union(u, v):
            if u == v:
                return
            
            if rank[u] < rank[v]:
                parent[u] = v
            elif rank[v] < rank[u]:
                parent[v] = u
            else:
                parent[u] = v
                rank[v] += 1
        
        res = []
        for x, y in edges:
            u, v = findRoot(x), findRoot(y)
            if u == v:
                res = [x, y]
            union(u, v)
        
        return res
        
