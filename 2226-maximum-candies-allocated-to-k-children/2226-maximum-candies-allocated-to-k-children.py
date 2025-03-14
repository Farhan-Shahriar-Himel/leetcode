class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        
        def isPossible(amount):
            if amount == 0:
                return True
            taken = 0
            for num in candies:
                taken += num // amount
            return taken >= k
        
        l, r = 0, max(candies)
        while l <= r:
            mid = l + (r - l) // 2
            if isPossible(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return r
        

