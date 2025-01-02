class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        preCalc = [0]
        vowel = {'a', 'e', 'i', 'o', 'u'}
        for i, word in enumerate(words):
            if word[0] in vowel and word[-1] in vowel:
                preCalc.append(preCalc[-1] + 1)
            else:
                preCalc.append(preCalc[-1])
        
        res = []
        for l, r in queries:
            l += 1
            r += 1
            res.append(preCalc[r] - preCalc[l - 1])
        
        return res