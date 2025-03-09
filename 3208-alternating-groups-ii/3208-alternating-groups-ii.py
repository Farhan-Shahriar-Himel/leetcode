class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        
        i, res = 0, 0
        for j in range(1, n + k - 1):
            if colors[j % n] == colors[(j - 1) % n]:
                i = j
            if j - i + 1 > k:
                i += 1
            if j - i + 1 == k:
                res += 1
        
        return res
