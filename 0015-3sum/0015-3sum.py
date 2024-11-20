class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            st = set()
            for j in range(i + 1, len(nums)):
                last = -(nums[i] + nums[j])
                if last in st:
                    ans.add(tuple(sorted([last, nums[i], nums[j]])))
                st.add(nums[j])
        return list(ans)