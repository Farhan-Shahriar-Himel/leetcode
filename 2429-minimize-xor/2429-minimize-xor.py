class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        setBits = 0
        for i in range(32):
            mask = (1 << i)
            setBits += 1 if (num2 & mask) != 0 else 0
        
        ans = 0
        for i in range(31, -1, -1):
            if setBits == 0:
                break
            mask = (1 << i)
            if num1 & mask != 0:
                ans |= mask
                setBits -= 1
        
        for i in range(32):
            if setBits == 0:
                break
            mask = (1 << i)
            if ans & mask == 0:
                ans |= mask
                setBits -= 1
        
        return ans

            