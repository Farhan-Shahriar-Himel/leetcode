class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        
        if numFriends == 1:
            return word
        
        n = len(word)
        large = max(word)
        res = "a"
        ln = numFriends - len(word) + 1
        for i, ch in enumerate(word):
            if ch == large:
                s = word[i: min(ln, n - i)]
                res = max(s, res)
        
        return res