class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 7)
        for b, e, d in shifts:
            if d == 1:
                diff[b + 1] += 1
                diff[e + 2] -= 1
            else:
                diff[b + 1] -= 1
                diff[e + 2] += 1
        
        for i in range(1, n + 1):
            diff[i] = diff[i - 1] + diff[i]
        diff = diff[1:]
        res = ""


        for i in range(n):
            now = ord(s[i]) - ord('a')
            new = (now + diff[i]) % 26
            res += chr(new + ord('a'))

        return res
