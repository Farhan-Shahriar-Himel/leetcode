class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            setBit = 0
            for num in nums:
                if num & (1 << i) != 0:
                    setBit += 1
            if setBit % 3 == 1:
                ans = ans | (1 << i)
        
        return ans - (1 << 32) if ans >= (1 << 31) else ans