class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {'(': ')', '{': '}', '[': ']'}

        for el in s:
            if len(stack) != 0 and stack[-1] in closing and el == closing[stack[-1]]:
                stack.pop()
            else:
                stack.append(el)
        
        return len(stack) == 0