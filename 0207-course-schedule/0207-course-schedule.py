from collections import defaultdict as dd

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = dd(list)
        for course, pre in prerequisites:
            preReq[course].append(pre)
        
        
        taken = set()

        def dfs(crs):
            if not preReq[crs]:
                return True
            if crs in taken:
                return False

            taken.add(crs)
            
            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
            
            return True
                

        for course in range(numCourses):
            if course in taken: continue
            if not dfs(course):
                return False
        
        return True
