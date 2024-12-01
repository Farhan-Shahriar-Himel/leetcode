# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = postorder[-1]
        mid = 0
        
        while inorder[mid] != root:
            mid += 1

        left_in = inorder[:mid]
        right_in = inorder[mid + 1:]

        left_post = postorder[:mid]
        right_post = postorder[mid:-1]

        rootNode = TreeNode(root)
        rootNode.left = self.buildTree(left_in, left_post)
        rootNode.right = self.buildTree(right_in, right_post)

        return rootNode