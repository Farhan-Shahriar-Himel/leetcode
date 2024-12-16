from heapq import heapify, heappush as push, heappop as pop

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)

        while k:
            num, i = pop(heap)
            nums[i] *= multiplier
            push(heap, (nums[i], i))
            k -= 1
        

        return nums
