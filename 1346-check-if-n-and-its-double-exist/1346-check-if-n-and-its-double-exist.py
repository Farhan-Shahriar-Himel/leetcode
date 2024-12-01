class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        newAr = set([2 * i for i in arr])
        zero = 0
        for el in arr:
            if zero == 0 and el == 0:
                zero += 1
            elif el in newAr:
                return True

        return False
