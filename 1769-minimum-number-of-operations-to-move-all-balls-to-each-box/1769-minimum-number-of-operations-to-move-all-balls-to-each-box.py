class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        pref = [0]
        suff = [0]
        one = 0
        for i in range(n):
            pref.append(pref[-1] + one)
            if boxes[i] == '1':
                one += 1

        one = 0
        for i in range(n - 1, -1, -1):
            suff.append(suff[-1] + one)
            if boxes[i] == '1':
                one += 1
        
        pref, suff = pref[1:], suff[::-1]

        return [pref[i] + suff[i] for i in range(n)]
        