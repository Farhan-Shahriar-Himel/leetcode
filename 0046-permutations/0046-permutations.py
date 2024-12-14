from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, tmp, visit = [], [], set()
        
        def backtrack():
            if len(tmp) == n:
                res.append(tmp[:])
            else:
                for i in range(n):
                    if i not in visit:
                        visit.add(i)
                        tmp.append(nums[i])
                        backtrack()
                        visit.remove(i)
                        tmp.pop()
        backtrack()
        
        return res