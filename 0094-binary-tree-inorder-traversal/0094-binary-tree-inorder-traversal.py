# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    tmp = []
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            self.tmp.append(root.val)
            self.inOrder(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.tmp.clear()
        self.inOrder(root)
        return self.tmp