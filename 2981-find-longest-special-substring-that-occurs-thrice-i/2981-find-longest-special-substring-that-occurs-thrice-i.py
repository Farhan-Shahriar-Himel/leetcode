from collections import defaultdict as hashMap

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        def checked(size):
            counter = hashMap(int)
            for i in range(n - size + 1):
                subS = s[i:i + size]
                counter[subS] += 1
                if counter[subS] == 3 and len(set(subS)) == 1:
                    return True
            return False
        
        l, r = 1, n - 1
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if checked(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return res