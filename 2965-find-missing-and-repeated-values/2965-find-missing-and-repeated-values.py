class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq = dict()
        res = []
        for row in grid:
            for num in row:
                if num not in freq:
                    freq[num] = True
                else:
                    res.append(num)
            
        n = len(grid)
        for num in range(1, n * n + 1):
            if num not in freq:
                res.append(num)
                break
        
        return res