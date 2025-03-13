class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def isPossible(k):
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                diff[r + 1] -= v
            
            tot = 0
            for i in range(n):
                tot += diff[i]
                if tot < nums[i]:
                    return False
            
            return True

        left, right = 0, len(queries)
        
        if not isPossible(right):
            return -1

        while left <= right:
            mid = (left + right) // 2
            if isPossible(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left