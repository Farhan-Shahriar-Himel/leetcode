"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned = dict()
        def dfs_clone(root):
            if root in cloned:
                return cloned[root]
            
            new = Node(root.val)
            cloned[root] = new
            for neighbor in root.neighbors:
                new_neighbor = dfs_clone(neighbor)
                new.neighbors.append(new_neighbor)
            
            return cloned[root]
        
        return dfs_clone(node)
            
        
