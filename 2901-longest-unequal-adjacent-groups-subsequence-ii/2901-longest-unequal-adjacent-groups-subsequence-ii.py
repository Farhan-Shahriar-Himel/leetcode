class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        n = len(words)

        def hamDist(a, b):
            nn = len(a)
            if (nn != len(b)):
                return False
            ok = True
            for i in range(nn):
                if a[i] != b[i]:
                    if ok:
                        ok = False
                    else:
                        return False
            return True
        
        dp = [1] * (n + 7)
        prev = [-1] * (n + 7)
        mx_i, mx = 0, 0

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and hamDist(words[i], words[j]):
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            
            if mx < dp[i]:
                mx = dp[i]
                mx_i = i

        res = []
        while prev[mx_i] != -1:
            res.append(words[mx_i])
            mx_i = prev[mx_i]
        res.append(words[mx_i])
        
        return res[::-1]