class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        dp = dict()

        def isPossible(i, j):
            if i + j >= len(s3) and i >= n and j >= m:
                return True

            if (i, j) in dp:
                return dp[(i, j)]
            
            pos = False
            if i < n and i + j < len(s3) and s1[i] == s3[i + j]:
                pos |= isPossible(i + 1, j)
            if j < m and i + j < len(s3) and s2[j] == s3[i + j]:
                pos |= isPossible(i, j + 1)
            
            dp[(i, j)] = pos
            return dp[(i, j)]

        return isPossible(0, 0)