"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def build(n, r, c):
            same = True
            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[r][c] != grid[i][j]:
                        same = False
                        break
            
            if same:
                return Node(grid[r][c], True)
            
            n //= 2
            topleft = build(n, r, c)
            topright = build(n, r, c + n)
            bottomleft = build(n, r + n, c)
            bottomright = build(n, r + n, c + n)

            return Node(0, False, topleft, topright, bottomleft, bottomright)
        
        return build(len(grid), 0, 0)