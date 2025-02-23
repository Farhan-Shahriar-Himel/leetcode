# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        def construct(i, j, k, l):
            if i > j or k > l:
                return None
            
            head = TreeNode(preorder[i])
            if i != j:
                x = postorder.index(preorder[i + 1])
                l_len = x - k + 1
                head.left = construct(i + 1, i + l_len, k, x)
                head.right = construct(i + l_len + 1, j, x + 1, l - 1)
            return head
        
        return construct(0, n - 1, 0, n - 1)
        