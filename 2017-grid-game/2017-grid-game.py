class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def calcPartial(matrix):
            partial = [[], [0]]
            row = len(matrix)
            col = len(matrix[0])
            for i in range(row):
                for j in range(col):
                    if partial[i]:
                        partial[i].append(partial[i][-1] + matrix[i][j])
                    else:
                        partial[i].append(matrix[i][j])
            partial[0] = partial[0][::-1]
            partial[0].append(0)
            return partial


        tmp = []
        tmp.append(grid[0][::-1])
        tmp.append(grid[1])

        preCalc = calcPartial(tmp)

        res = float('inf')
        for i in range(m):
            res = min(res, max(preCalc[0][i + 1], preCalc[1][i]))

        return res        
        