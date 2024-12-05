# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        avgs = []
        def bfs(root):
            q = deque()
            q.append(root)
            while q:
                n = len(q)
                tot = 0
                for i in range(n):
                    par = q.popleft()
                    tot += par.val
                    if par.left:
                        q.append(par.left)
                    if par.right:
                        q.append(par.right)
                avgs.append(tot / n)
            
        bfs(root)
        return avgs