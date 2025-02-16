class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * ((n * 2) - 1)
        taken = set()

        def build(idx):
            while idx < len(res) and res[idx] != 0:
                idx += 1
            if idx >= len(res):
                return True

            for i in range(n, 0, -1):
                if i in taken:
                    continue
                if i == 1:
                    res[idx] = 1
                    taken.add(i)
                    if build(idx + 1):
                        return True
                    res[idx] = 0
                    taken.remove(i)
                if idx + i < len(res) and res[idx] == 0 and res[idx + i] == 0:
                    res[idx] = res[idx + i] = i
                    taken.add(i)
                    if build(idx + 1):
                        return True
                    res[idx] = res[idx + i] = 0
                    taken.remove(i)
        
        build(0)

        return res

        