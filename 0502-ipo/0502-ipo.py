from heapq import heapify, heappush as push, heappop as pop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted([(capital[i], profit) for i, profit in enumerate(profits)])
        heap, i = [], 0
        while k:
            if i < len(projects):
                for cap, profit in projects[i:]:
                    if cap <= w:
                        push(heap, -profit)
                        i += 1
                    else:
                        break

            if not heap: 
                return w

            w += -1 * (pop(heap))
            k -= 1
        
        return w