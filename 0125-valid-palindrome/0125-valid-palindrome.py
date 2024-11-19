class Solution:
    def check(self, ch):
        return 'a' <= ch <= 'z' or '0' <= ch <= '9'

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        for el in s:
            if self.check(el):
                new_s += el
                
        i, j = 0, len(new_s) - 1
        while i < j:
            if new_s[i] != new_s[j]:
                return False
            i += 1
            j -= 1
        
        return True