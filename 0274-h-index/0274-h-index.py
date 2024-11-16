class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        n = len(citations)
        for i in range(n):
            c = n - i
            if citations[i] >= c:
                h = c
                break

        return h