from heapq import heappush as push, heappop as pop, heapify

class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = {-1,}
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)

        score = 0
        while heap:
            indx = -1
            smallest = 0
            while heap and indx in marked:
                smallest, indx = pop(heap)
            
            if not heap:
                break
            
            score += smallest
            marked.add(indx)
            marked.add(indx - 1)
            marked.add(indx + 1)
        
        return score