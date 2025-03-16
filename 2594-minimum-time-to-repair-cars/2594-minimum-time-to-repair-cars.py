class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        mn_rank = min(ranks)

        def isPossible(t):
            cnt = 0
            for r in ranks:
                cnt += int(sqrt(t // r))
            return cnt >= cars

        l, r = 1, mn_rank * cars * cars
        while l <= r:
            mid = (l + r) // 2
            if isPossible(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l