from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magChar = Counter(magazine)
        ransChar = Counter(ransomNote)

        for key in ransChar.keys():
            if ransChar[key] > magChar[key]:
                return False
        
        return True