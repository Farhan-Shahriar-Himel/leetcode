from heapq import heappush as push, heappop as pop

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        res, heap, taken = [], [(nums1[0] + nums2[0], 0, 0)], {(0, 0)}

        for _ in range(k):
            val, i, j = pop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2) and (i, j + 1) not in taken:
                push(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                taken.add((i, j + 1))
            if i + 1 < len(nums1) and (i + 1, j) not in taken:
                push(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                taken.add((i + 1, j))      

        return res     
            