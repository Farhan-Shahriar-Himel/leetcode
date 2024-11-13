class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        index = [ind for ind, el in enumerate(number) if el == digit]
        ans = max(int(number[:i] + number[i + 1:]) for i in index)
        return str(ans)