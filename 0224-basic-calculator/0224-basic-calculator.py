class Solution:
    def removeBraces(self, s):
        stack = ['+']
        ans = ""
        for i, tkn in enumerate(s):
            if tkn.isdigit():
                ans += tkn
            elif tkn == '+' or tkn == '-':
                sign = stack[-1]
                if sign == tkn:
                    ans += '+'
                else:
                    ans += '-'
            else:
                if tkn == '(':
                    sign = '+'
                    if i > 0:
                        if s[i - 1] == '-':
                            sign = '-'
                    sign = '+' if stack[-1] == sign else '-'
                    stack.append(sign)
                else:
                    stack.pop()
        
        return ans
                    

    def calculate(self, s: str) -> int:
        s = self.removeBraces("".join(s.split()))
        add = True if s[0] != '-' else False
        i, num, res, n = 0, 0, 0, len(s)

        while i < n:
            if s[i] == '+':
                add = True
            elif s[i] == '-':
                add = False
            else:
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                if add: res += num
                else: res -= num
                num = 0
                i -= 1
            i += 1

        return res