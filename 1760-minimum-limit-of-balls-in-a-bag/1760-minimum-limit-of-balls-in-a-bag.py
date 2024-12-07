class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()
        l, r = 1, nums[-1]
        res = -1

        def give_count(num, x):
            res = num // x
            if num % x == 0:
                res -= 1
            return res

        def ok(x):
            cnt = 0
            for num in nums:
                if num > x:
                    cnt += give_count(num, x) 
                    if cnt > maxOperations:
                        return False
            return True

        while l <= r:
            mid = l + (r - l) // 2
            if ok(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res