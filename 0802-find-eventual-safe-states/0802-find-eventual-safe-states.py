class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = dict()

        def dfs(node):
            if node in safe:
                return safe[node]

            safe[node] = False
            for child in graph[node]:
                if not dfs(child):
                    return False
            
            safe[node] = True
            return True
        
        res = []
        for node in range(n):
            if dfs(node):
                res.append(node)
        
        return res

