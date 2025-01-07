class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(reverse=True, key=len)
        res = []
        for i, word in enumerate(words):
            i -= 1
            while i >= 0:
                if word in words[i]:
                    res.append(word)
                    break
                i -= 1
        return res