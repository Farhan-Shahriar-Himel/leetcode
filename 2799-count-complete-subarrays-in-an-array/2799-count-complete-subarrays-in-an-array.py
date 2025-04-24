class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 0
        mp = defaultdict(int)
        target = len(set(nums))
        res = 0
        while True:
            if len(mp) == target:
                res += (n - j + 1)
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1
            elif j < n:
                mp[nums[j]] += 1
                j += 1
            else:
                break
        
        return res