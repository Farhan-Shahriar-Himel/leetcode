class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        def inc(i):
            return i % n
        
        def check(idx):
            i = idx
            while i != inc(idx - 1):
                j = inc(i + 1)
                if nums[i] > nums[j]:
                    return False
                i = j
            return True


        for i in range(n):
            if check(i):
                return True
        
        return False