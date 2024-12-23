# Definition for a binary tree node.7
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q, res = [root], 0
        while q:
            nodes, q = q, []
            seq = sorted(nodes, key=lambda x: x.val)
            cnt = 0
            for i, node in enumerate(nodes):
                if node.val != seq[i].val:
                    cnt += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res += (cnt + 1) // 2
        
        return res
                
