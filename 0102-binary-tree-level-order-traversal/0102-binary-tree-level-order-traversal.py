# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        node_list = []
        def bfs(root):
            q = deque()
            q.append(root)
            while q:
                n = len(q)
                nodes = []
                for i in range(n):
                    par = q.popleft()
                    nodes.append(par.val)
                    if par.left:
                        q.append(par.left)
                    if par.right:
                        q.append(par.right)
                node_list.append(nodes)
            
        
        bfs(root)

        return node_list
