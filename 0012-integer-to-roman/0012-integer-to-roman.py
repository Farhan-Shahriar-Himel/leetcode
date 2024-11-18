class Solution:
    def __init__(self):
        self.rank = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    
    def roman(self, target):
        ind = []
        i = 0
        while i < len(self.rank):
            if self.rank[i][0] <= target:
                ind.append(i)
                target -= self.rank[i][0]
                i -= 1
            i += 1

        res = []
        for el in ind:
            res.append(self.rank[el][1])
        
        return "".join(res)



    def intToRoman(self, num: int) -> str:
        nums = []
        s = list(str(num))[::-1]
        while len(s) > 0:
            nums.append(int(s[-1]) * (10 ** (len(s) - 1)))
            s.pop()
        
        res = []
        for el in nums:
            res.append(self.roman(int(el)))

        return "".join(res)