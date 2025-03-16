class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        mn_rank = min(ranks)

        def isPossible(t):
            cnt = 0
            for r in ranks:
                cnt += int(sqrt(t // r))
            return cnt >= cars

        l, r = 1, mn_rank * cars * cars
        while r - l > 1:
            mid = l + (r - l) // 2
            if isPossible(mid):
                r = mid
            else:
                l = mid + 1
        
        return r