class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        original = [0] * n
        
        if n == 1:
            if derived[0] == 0:
                return True
            return False

        if derived[0] == 1:
            original[0] = 0
            original[1] = 1 
        else:
            original[0] = original[1] = 0

        for i in range(1, n):
            if derived[i] == 1:
                original[(i + 1) % n] = original[i] ^ 1
            else:
                original[(i + 1) % n] = original[i]
        
        return original[0] == 0