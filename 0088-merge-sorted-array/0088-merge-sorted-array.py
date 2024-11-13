class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n = len(nums1) - len(nums2)
        t1 = nums1[:n]
        t1.append(1e9 + 7)
        nums2.append(1e9 + 7)
        ind = 0
        lp = rp = 0
        while (ind < len(nums1)):
            if (t1[lp] < nums2[rp]):
                nums1[ind] = t1[lp]
                lp += 1
                ind += 1
            else:
                nums1[ind] = nums2[rp]
                rp += 1
                ind += 1