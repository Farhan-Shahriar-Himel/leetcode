class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        carry, res = 0, ""
        for i in range(max(len(a), len(b)) + 1):
            x, y = '0', '0'
            if i < len(a): x = a[i]
            if i < len(b): y = b[i]
            if x == y == '0':
                if carry > 0:
                    res += '1'
                    carry = 0
                else:
                    res += '0'
            elif (x == '1' and y == '0') or (x == '0' and y == '1'):
                if carry > 0:
                    res += '0'
                else:
                    res += '1'
            elif x == y == '1':
                if carry > 0:
                    res += '1'
                else:
                    res += '0'
                    carry = 1
        
        return res[::-1] if res[-1] == '1' else res[::-1][1:]