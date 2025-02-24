class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = dict()
        def dfs(node, par, time):
            if node == 0:
                visited[node] = time
                return True
            for child in adj[node]:
                if child == par:
                    continue
                if dfs(child, node, time + 1):
                    visited[node] = time
                    return True
            return False
        
        dfs(bob, -1, 0)

        q = deque([(0, -1, 0, amount[0])])
        res = -float('inf')
        while q:
            node, par, time, profit = q.popleft()
            if len(adj[node]) == 1 and node != 0:
                    res = max(res, profit)
            for child in adj[node]:
                if child == par:
                    continue
                child_time = time + 1
                child_profit = amount[child]
                if child in visited:
                    if child_time > visited[child]:
                        child_profit = 0
                    elif child_time == visited[child]:
                        child_profit //= 2
                
                q.append((child, node, child_time, profit + child_profit))
                
        return res