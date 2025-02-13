class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapify(nums)
        res = 0
        while len(nums) > 1:
            x, y = heappop(nums), heappop(nums)
            if min(x, y) >= k:
                return res
            heappush(nums, min(x, y) * 2 + max(x, y))
            res += 1
        
        return n - 1
            