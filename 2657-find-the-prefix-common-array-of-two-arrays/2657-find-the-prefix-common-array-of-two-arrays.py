class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA, setB = set(), set()
        c = [0]

        for i in range(len(A)):
            setA.add(A[i])
            setB.add(B[i])
            if A[i] == B[i]:
                c.append(c[-1] + 1)
            elif A[i] in setB and B[i] in setA:
                c.append(c[-1] + 2)
            elif A[i] in setB or B[i] in setA:
                c.append(c[-1] + 1)
            else:
                c.append(c[-1])
        
        return c[1:]