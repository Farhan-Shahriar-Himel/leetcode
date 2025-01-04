class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        taken = set()
        res = 0
        for i in range(len(s)):
            if s[i] not in taken:
                j = s.rindex(s[i])
                letters = set()
                for k in range(i + 1, j):
                    letters.add(s[k])
                res += len(letters)
                taken.add(s[i])

        return res     
