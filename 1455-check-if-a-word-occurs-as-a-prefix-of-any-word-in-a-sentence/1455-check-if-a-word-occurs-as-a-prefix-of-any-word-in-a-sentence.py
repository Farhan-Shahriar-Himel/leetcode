class Solution:
    def findPref(self, word, searchWord):
        if len(word) < len(searchWord):
            return False
        
        for i in range(len(word)):
            if word[i] != searchWord[i]:
                return False
            if i == len(searchWord) - 1:
                return True
        
        return True

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, word in enumerate(words):
            if self.findPref(word, searchWord):
                return i + 1
        
        return -1