# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        stack, i, cnt = [], 0, 0
        while i < n:
            if traversal[i] == '-':
                cnt += 1
                i += 1
            else:
                digit = ""
                while i < n and traversal[i] != '-':
                    digit += traversal[i]
                    i += 1
                node = TreeNode(int(digit))
                
                while len(stack) > cnt:
                    stack.pop()
                
                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
                stack.append(node)
                cnt = 0
    
        return stack[0]
        
                
        
