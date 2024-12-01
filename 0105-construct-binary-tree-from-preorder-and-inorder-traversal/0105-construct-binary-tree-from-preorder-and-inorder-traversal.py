# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = preorder[0]
        
        i, root_ind = 0, -1
        mid = 0
        while inorder[mid] != root:
            mid += 1
        
        left_in = inorder[0: mid]
        right_in = inorder[mid + 1:]

        left_pre = preorder[1: mid + 1]
        right_pre = preorder[mid + 1:]

        root_node = TreeNode(root)
        root_node.left = self.buildTree(left_pre, left_in)
        root_node.right = self.buildTree(right_pre, right_in)

        return root_node   