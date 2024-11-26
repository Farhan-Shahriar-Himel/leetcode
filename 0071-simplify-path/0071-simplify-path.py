class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for el in path:
            if el == '' or el == '.':
                continue
            if el == '..':
                if stack: stack.pop()
            else:
                stack.append(el)
        
        return '/' + "/".join(stack)