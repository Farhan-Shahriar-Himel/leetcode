class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n, q = len(prerequisites), len(queries)
        parent = defaultdict(list)
        for u, v in prerequisites:
            parent[v].append(u)

        visit = set()

        def dfs(u, v):
            if u == v:
                return True
            visit.add(v)
            for child in parent[v]:
                if child in visit:
                    continue
                if dfs(u, child):
                    return True
            return False
        
        res = []
        for u, v in queries:
            if dfs(u, v):
                res.append(True)
            else:
                res.append(False)
            visit = set()
        

        return res