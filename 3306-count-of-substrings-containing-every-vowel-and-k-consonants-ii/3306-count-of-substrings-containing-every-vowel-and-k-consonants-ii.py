class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        def atleast(d):
            vowel = defaultdict(int)
            cons = 0
            res, l = 0, 0
            for r in range(n):
                if word[r] in "aeiou":
                    vowel[word[r]] += 1
                else:
                    cons += 1

                while len(vowel) == 5 and cons >= d:
                    res += n - r
                    if word[l] in "aeiou":
                        vowel[word[l]] -= 1
                    else:
                        cons -= 1
                    if vowel[word[l]] == 0:
                        vowel.pop(word[l])
                    l += 1
            return res

        return atleast(k) - atleast(k + 1) 
