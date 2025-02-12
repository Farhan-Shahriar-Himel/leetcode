class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for num in nums:
            sm = sum(map(int, str(num)))
            d[sm].append(num);
            d[sm].sort(reverse=True)
            if len(d[sm]) > 2:
                d[sm].pop()
        
        res = -1
        for k, v in d.items():
            if len(v) < 2:
                continue
            res = max(res, sum(v))
        
        return res
        