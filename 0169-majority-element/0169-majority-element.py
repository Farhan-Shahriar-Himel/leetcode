class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = target = 0
        for el in nums:
            if cnt == 0:
                target = el
                cnt += 1
            elif el != target:
                cnt -= 1
            else:
                cnt += 1
        return target