class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = [i for i in range(1, n + 2)]

        def valid(a):
            for i in range(n):
                if pattern[i] == 'I' and a[i] > a[i + 1]:
                    return False
                elif pattern[i] == 'D' and a[i] < a[i + 1]:
                    return False
            return True

        for p in permutations(res):
            if p == (1, 2, 3, 5, 4, 9, 8, 7, 6):
                print(p)
            if valid(p):
                return "".join(map(str, p))
        
        return "Saira den vai"