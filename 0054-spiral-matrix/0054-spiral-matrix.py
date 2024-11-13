class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        op = ["right", "bottom", "left", "top"]
        n = len(matrix)
        m = len(matrix[0])
        left = top = 0
        right = m - 1
        bottom = n - 1
        ind = 0
        ans = []
        while True:
            cnt = False
            if op[ind] == "right":
                for i in range(left, right + 1, 1):
                    print(matrix[top][i], end=" ")
                    ans.append(matrix[top][i])
                    cnt = True
                top += 1
            elif op[ind] == "bottom":
                for i in range(top, bottom + 1, 1):
                    print(matrix[i][right], end=" ")
                    ans.append(matrix[i][right])
                    cnt = True
                right -= 1
            elif op[ind] == "left":
                for i in range(right, left - 1, -1):
                    print(matrix[bottom][i], end=" ")
                    ans.append(matrix[bottom][i])
                    cnt = True
                bottom -= 1
            else:
                for i in range(bottom, top - 1, -1):
                    print(matrix[i][left], end=" ")
                    ans.append(matrix[i][left])
                    cnt = True
                left += 1
            ind = (ind + 1) % 4
            if not cnt:
                break
        
        return ans
