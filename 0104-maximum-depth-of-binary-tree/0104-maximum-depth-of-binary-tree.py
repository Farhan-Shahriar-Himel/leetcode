# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        deapth = 0
        def dfs(head):
            if head is None:
                return 0
            leftNode = head.left
            rightNode = head.right
            d1 = 1 + dfs(leftNode)
            d2 = 1 + dfs(rightNode)
            return max(d1, d2)
        
        res = dfs(root)

        return res