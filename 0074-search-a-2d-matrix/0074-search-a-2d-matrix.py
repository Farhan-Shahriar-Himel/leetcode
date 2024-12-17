from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left = 0; right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                ind = bisect_left(matrix[mid], target)
                return True if matrix[mid][ind] == target else False
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
