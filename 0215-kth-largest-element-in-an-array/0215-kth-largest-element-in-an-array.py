from heapq import heapify, heappop as pop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        res, k = 0, len(nums) - k + 1
        while nums and k:
            res = pop(nums)
            k -= 1
        return res
