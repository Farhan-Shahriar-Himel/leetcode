from heapq import heappush as push, heappop as pop, heapify
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-num for num in gifts]
        heapify(gifts)

        while k > 0:
            val = -1 * pop(gifts)
            val = int(val ** 0.5)
            push(gifts, -1 * val)
            k -= 1
        
        return sum(gifts) * -1