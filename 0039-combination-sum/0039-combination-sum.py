class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, tmp, n = [], [], len(candidates)
        
        def backtrack(begin, total):
            if total == 0:
                res.append(tmp.copy())
            else:
                for i in range(begin, n):
                    num = candidates[i]
                    if total - num >= 0:
                        tmp.append(num)
                        backtrack(i, total - num)
                        tmp.pop()
        
        backtrack(0, target)
        
        return res
