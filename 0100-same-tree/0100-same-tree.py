# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(r1, r2):
            if r1 is None and r2 is None:
                return True
            if (r1 is None or r2 is None or r1.val != r2.val):
                print(r1, r2)
                return False

            rLeft1 , rRight1 = r1.left, r1.right
            rLeft2, rRight2 = r2.left, r2.right

            return dfs(rLeft1, rLeft2) & dfs(rRight1, rRight2)
            
        
        return dfs(p, q)