from collections import defaultdict as dd

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indx = dd(list)
        for i in range(len(nums)):
            indx[nums[i]].append(i)
        
        for inds in indx.values():
            for i in range(len(inds) - 1):
                if abs(inds[i] - inds[i + 1]) <= k:
                    return True
        
        return False