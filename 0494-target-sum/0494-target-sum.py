class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = dict()

        def ways(i, tot):

            if (i, tot) in dp:
                return dp[(i, tot)]

            if i == len(nums):
                if tot == target:
                    return 1
                return 0
            
            type1 = ways(i + 1, tot + nums[i])
            type2 = ways(i + 1, tot - nums[i])

            dp[(i, tot)] = type1 + type2
            return dp[(i, tot)]
        

        return ways(0, 0)

        return res[0]