# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')

        def get_result(head):
            nonlocal res
            if not head:
                return 0
            
            leftMax = max(get_result(head.left), 0)
            rightMax = max(get_result(head.right), 0)

            res = max(res, head.val + leftMax + rightMax)

            return head.val + max(leftMax, rightMax)

        get_result(root)

        return res
        
