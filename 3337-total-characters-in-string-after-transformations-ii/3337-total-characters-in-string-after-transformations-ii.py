class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9 + 7
        T = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for move in range(1, nums[i] + 1):
                T[i][(i + move) % 26] += 1
        
        def multiplyMatrix(m1, m2):
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        res[i][j] = (res[i][j] + (m1[i][k] * m2[k][j]) % mod) % mod
            return res
        
        def matrixPower(matrix, exp):
            res = [[1 if i == j else 0 for i in range(26)] for j in range(26)]
            while exp > 0:
                if exp & 1 != 0:
                    res = multiplyMatrix(res, matrix)
                matrix = multiplyMatrix(matrix, matrix)
                exp >>= 1
            return res


        Tp = matrixPower(T, t)

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        result = 0
        for i in range(26):
            if freq[i] == 0:
                continue
            for j in range(26):
                result = (result + (Tp[i][j] * freq[i]) % mod) % mod
        
        return result % mod