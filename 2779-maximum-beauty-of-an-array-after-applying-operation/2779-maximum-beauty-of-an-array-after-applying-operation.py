class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, n = 0, len(nums)

        for i in range(n):
            target, l, r, val = 0, 0, n - 1, nums[i] - 2 * k
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= val:
                    target = mid
                    r = mid - 1
                else:
                    l = mid + 1
            res = max(res, i - target + 1)

        return res