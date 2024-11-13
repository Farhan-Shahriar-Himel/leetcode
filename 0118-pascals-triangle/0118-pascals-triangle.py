class Solution:
    def get_row(self, n):
        a = [1]
        ans = 1
        for i in range(1, n):
            ans *= n - i
            ans //= i
            a.append(ans)
        return a

    def generate(self, numRows: int) -> List[List[int]]:
        a = []
        for i in range(1, numRows + 1):
            row = self.get_row(i)
            a.append(row)
        return a

