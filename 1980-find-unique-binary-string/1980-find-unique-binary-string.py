class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)        
        def increase(s):
            s, i = list(s), n - 1
            while i < n and s[i] != '0':
                s[i] = '0'
                i -= 1
            s[i] = '1'
            return "".join(s)
        
        mp = dict()
        for num in nums:
            mp[num] = True
        
        res = "0" * n
        while res in mp:
            res = increase(res)

        return res