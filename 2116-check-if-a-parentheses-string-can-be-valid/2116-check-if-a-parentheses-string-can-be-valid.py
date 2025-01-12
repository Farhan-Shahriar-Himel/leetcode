class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        
        free, braces = [], []
        for i in range(n):
            if locked[i] == '0':
                free.append(i)
            elif s[i] == '(':
                braces.append(i)
            elif s[i] == ')' and braces:
                braces.pop()
            elif s[i] == ')' and free:
                free.pop()
            else:
                return False
        
        while free and braces:
            if free[-1] < braces[-1]:
                return False
            free.pop()
            braces.pop()
        
        return not braces

                