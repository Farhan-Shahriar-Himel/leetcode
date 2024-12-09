from collections import defaultdict as dd

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = dd(list)
        for course, pre in prerequisites:
            preReq[course].append(pre)
        
        sequence, visited, taken = [], set(), set()

        def dfs(crs):
            if crs in visited:
                return False
            if crs in taken:
                return True
            visited.add(crs)
            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            taken.add(crs)
            sequence.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return sequence