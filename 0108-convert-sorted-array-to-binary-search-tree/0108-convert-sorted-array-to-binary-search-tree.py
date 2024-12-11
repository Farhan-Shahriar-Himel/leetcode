# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0: return None
        indx = n // 2
        root = TreeNode(nums[indx])
        root.left = self.sortedArrayToBST(nums[:indx])
        root.right = self.sortedArrayToBST(nums[indx + 1:])
        return root