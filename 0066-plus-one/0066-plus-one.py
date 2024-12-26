class Solution:
    def plusOne(self, a: List[int]) -> List[int]:
        a, ok = a[::-1], False
        for i in range(len(a)):
            if a[i] + 1 < 10:
                a[i] += 1
                ok = True
                break
            a[i] = 0
        
        if not ok:
            a.append(1)

        return a[::-1]
            