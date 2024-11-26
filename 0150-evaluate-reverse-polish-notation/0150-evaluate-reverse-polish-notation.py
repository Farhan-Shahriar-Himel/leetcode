class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for tkn in tokens:
            if tkn in operators:
                b = stack.pop()
                a = stack.pop()
                res = int(eval(a + tkn + b))
                stack.append(str(res))
            else:
                stack.append(tkn)
            
        return int(stack[0])