class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for el in nums:
            if el - 1 not in nums:
                ln = 1
                while el + ln in nums:
                    ln += 1

                res = max(res, ln)
        
        return res