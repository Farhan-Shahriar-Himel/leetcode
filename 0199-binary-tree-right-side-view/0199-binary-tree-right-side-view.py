# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        rightView = []
        
        def bfs(root):
            q = deque()
            q.append(root)
            while q:
                n = len(q)
                for i in range(n):
                    par = q.popleft()
                    if par.left:
                        q.append(par.left)
                    if par.right:
                        q.append(par.right)
                    if i == n - 1:
                        rightView.append(par.val)
        
        bfs(root)
        
        return rightView