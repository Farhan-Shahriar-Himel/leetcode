class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        for el in nums:
            if el == 0:
                zeros += 1
            else:
                prod *= el
        
        if zeros > 1:
            return [0] * len(nums)
        
        res = []
        if zeros == 1:
            for el in nums:
                if el == 0:
                    res.append(prod)
                else:
                    res.append(0) 
            return res

        for el in nums:
            res.append(prod // el)
        
        return res