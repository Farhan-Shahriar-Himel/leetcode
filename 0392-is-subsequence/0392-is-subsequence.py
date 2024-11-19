class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for el in s:
            found = False
            for i in range(j, len(t)):
                if t[i] == el:
                    found = True
                    j = i + 1
                    break
            if not found:
                return False

        return True