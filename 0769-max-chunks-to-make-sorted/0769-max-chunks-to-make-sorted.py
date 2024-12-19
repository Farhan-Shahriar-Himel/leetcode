class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        prefMax, suffMin = [], []
        for num in arr:
            if not prefMax or prefMax[-1] <= num:
                prefMax.append(num)
            else:
                prefMax.append(prefMax[-1])
        
        for num in arr[::-1]:
            if not suffMin or suffMin[-1] >= num:
                suffMin.append(num)
            else:
                suffMin.append(suffMin[-1])
        res = 1
        suffMin = suffMin[::-1]
        for i in range(len(arr) - 1, 0, -1):
            if prefMax[i - 1] <= suffMin[i]:
                res += 1

        return res