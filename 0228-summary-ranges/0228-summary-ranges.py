class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []

        res = []
        strt, n = nums[0], len(nums)

        for i in range(1, n + 1):
            if i == n or nums[i] - nums[i - 1] != 1:
                if strt != nums[i - 1]: 
                    s = str(strt) + '->' + str(nums[i - 1])
                    res.append(s)
                else:
                    res.append(str(strt))

                if i < n: strt = nums[i]

        return res