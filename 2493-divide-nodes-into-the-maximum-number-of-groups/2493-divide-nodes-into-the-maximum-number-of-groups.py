class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def get_components(src):
            q = deque([src])
            res = set()
            while q:
                par = q.popleft()
                res.add(par)
                for nei in adj[par]:
                    if nei in res:
                        continue
                    q.append(nei)
            return res

        def bfs(src):
            q = deque([src])
            level = {src: 1}
            state = {src: 1}
            while q:
                par = q.popleft()
                now = state[par] ^ 1
                for nei in adj[par]:
                    if nei in state:
                        if state[nei] != now:
                            return -1
                    if nei in level:
                        continue
                    q.append(nei)
                    level[nei] = level[par] + 1
                    state[nei] = now

            return max(level.values())
        
        visit = set()
        res = 0
        for i in range(1, n + 1):
            if i in visit:
                continue
            cmps = get_components(i)
            mx_grp = 0
            for node in cmps:
                visit.add(node)
                grp = bfs(node)
                if grp == -1:
                    return -1
                mx_grp = max(mx_grp, grp)
            res += mx_grp
        
        return res
            
