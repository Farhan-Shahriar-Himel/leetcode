class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n, groupElement, groupNo = len(nums), defaultdict(list), defaultdict(int)
        new = sorted(nums, reverse=True)

        groupElement[0].append(new[0])
        groupNo[0] = new[0]
        level = 0
        for i in range(1, n):
            if new[i - 1] - new[i] <= limit:
                groupElement[level].append(new[i])
                groupNo[new[i]] = level
            else:
                level += 1
                groupElement[level].append(new[i])
                groupNo[new[i]] = level

        res = []
        for i in range(n):
            lvl = groupNo[nums[i]]
            res.append(groupElement[lvl].pop())
        
        return res
        

        


        