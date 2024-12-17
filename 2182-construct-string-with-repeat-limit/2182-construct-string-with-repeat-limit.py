from collections import Counter
from heapq import heappush as push, heappop as pop, heapify

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        countOf = Counter(s)

        heap = [-ord(ch) for ch in countOf.keys()]
        heapify(heap)

        res = ""
        while heap:
            char = chr(-pop(heap))
            use = min(repeatLimit, countOf[char])
            res += char * use
            countOf[char] -= use

            if countOf[char] > 0:
                if not heap:
                    break
                nxtChar = chr(-pop(heap))
                res += nxtChar
                countOf[nxtChar] -= 1

                if countOf[nxtChar] > 0:
                    push(heap, -ord(nxtChar))
                
                push(heap, -ord(char))

        return res