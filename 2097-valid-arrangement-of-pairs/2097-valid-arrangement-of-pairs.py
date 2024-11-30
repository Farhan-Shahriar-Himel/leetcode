from collections import defaultdict as dd

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        edges = dd(list)
        track = dd(int)
        for src, dst in pairs:
            edges[src].append(dst)
            track[src] += 1
            track[dst] -= 1

        res = []
        def dfs(src):
            for child in edges[src]:
                edges.pop(src)
                res.append([src, child])
                dfs(child)
        
        node = pairs[0][0]
        for src in track:
            if track[src] == 1:
                node = src
                break
        
        dfs(node)
        
        return res

        

