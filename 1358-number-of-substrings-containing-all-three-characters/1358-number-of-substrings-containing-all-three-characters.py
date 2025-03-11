class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        word = defaultdict(int)
        i = 0
        for j in range(n):
            word[s[j]] += 1
            while len(word) == 3:
                res += n - j
                word[s[i]] -= 1
                if word[s[i]] == 0:
                    word.pop(s[i])
                i += 1
        
        return res
