class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        if len(str1) < len(str2):
            return False
        
        j = 0
        for i in range(len(str1)):
            if (str1[i] == 'z' and str2[j] == 'a') or (0 <= ord(str2[j]) - ord(str1[i]) <= 1):
                j += 1
                if j == len(str2):
                    return True

        return False