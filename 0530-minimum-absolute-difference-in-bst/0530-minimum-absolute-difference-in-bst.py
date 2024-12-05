# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        res = [float('inf')]
        prev = [None]
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            if prev[0] is not None:
                res[0] = min(res[0], abs(prev[0] - root.val))
            prev[0] = root.val
            dfs(root.right)
        
        dfs(root)

        return res[0]
