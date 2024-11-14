class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        new_nums = nums.copy()
        for el in new_nums:
            if el == val:
                tmp.append(el)
                nums.remove(val)
        nums = nums + tmp