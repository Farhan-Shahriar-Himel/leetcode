class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prevErr = [0] * n
        for i in range(1, n):
            if nums[i] % 2 == nums[i - 1] % 2:
                prevErr[i] = prevErr[i - 1] + 1
            else:
                prevErr[i] = prevErr[i - 1]

        return [prevErr[l] == prevErr[r] for l, r in queries]