class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, visited = [], set()
        charMap = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

            
        def combine(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
            else:
                for ch in charMap[digits[i]]:
                    combine(i + 1, curr + ch)
        

        combine(0, "")

        return res if res[0] else []