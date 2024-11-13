class Solution:
    from collections import defaultdict

    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = 0
        mp = defaultdict(int)
        mp[0] = 1
        ans = 0
        for el in nums:
            pref += el
            diff = pref - k
            ans += mp[diff]
            mp[pref] += 1

        return ans