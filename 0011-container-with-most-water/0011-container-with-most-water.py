class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j, ans = 0, n - 1, 0
        while i < j:
            d = j - i
            ans = max(ans, d * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return ans