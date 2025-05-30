class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        adj = [[] for _ in range(n + 3)]

        for u, v in enumerate(edges):
            if v == -1:
                continue
            adj[u].append(v)
        
        vis1, vis2 = set(), set()
        dist1, dist2 = [float('inf')] * (n + 7), [float('inf')] * (n + 7)

        def bfs(src, dist):
            q = deque([src])
            dist[src] = 0
            while q:
                par = q.popleft()
                for child in adj[par]:
                    if dist[child] != float('inf'):
                        continue
                    dist[child] = dist[par] + 1
                    q.append(child)
        
        bfs(node1, dist1)
        bfs(node2, dist2)

        res = -1
        mn_dist = float('inf')
        for node in range(n):
            mn = max(dist1[node], dist2[node])
            if mn < mn_dist:
                mn_dist = mn
                res = node

        return res 