class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        x, y = len(s1), len(s2)
        table = [[0] * (y + 1) for _ in range(x + 1)]
        
        for i in range(1, x + 1):
            for j in range(1, y + 1):
                if s1[i-1] == s2[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        
        i, j = x, y
        res = []
        
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                res.append(s1[i-1])
                i -= 1
                j -= 1
            elif table[i-1][j] >= table[i][j-1]:
                res.append(s1[i-1])
                i -= 1
            else:
                res.append(s2[j-1])
                j -= 1
        
        res.extend(s1[:i][::-1])
        res.extend(s2[:j][::-1])
        
        return ''.join(res[::-1])