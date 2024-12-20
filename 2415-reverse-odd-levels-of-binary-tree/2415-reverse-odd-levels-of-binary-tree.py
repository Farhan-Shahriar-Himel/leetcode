# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q, lvl = deque(), 0
        q.append(root)
        while q:
            nodes, n, q = list(q), len(q), deque()

            if lvl & 1:
                j = n - 1
                for i in range(n // 2): 
                    nodes[i].val, nodes[j].val = nodes[j].val, nodes[i].val
                    j -= 1

            for node in nodes:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl += 1
        
        return root

                    