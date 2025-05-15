class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        res = [words[0]]
        prev = groups[0]

        def make(i):
            if i >= n:
                return
            if prev != groups[i]:
                res.append(words[i])
                prev = groups[i]
            make(i + 1)    

        make(1)

        return res