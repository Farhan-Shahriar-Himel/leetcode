from heapq import heappush as push, heappop as pop, heapify

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def get_inc(x, y):
            curr = x / y
            new = (x + 1) / (y + 1)
            return new - curr

        heap = [(-get_inc(x, y), x, y) for x, y in classes]
        heapify(heap)
        
        while extraStudents:
            inc, pas, tot = pop(heap)
            push(heap, (-get_inc(pas + 1, tot + 1), pas + 1, tot + 1))
            extraStudents -= 1

        res = 0
        for inc, pas, tot in heap:
            res += pas / tot
        
        return res / len(classes)
        
