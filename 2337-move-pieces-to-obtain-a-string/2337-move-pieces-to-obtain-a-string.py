class Solution:

    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        start += '#'
        target += '#'
        i = j = 0
        while i < n or j < n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1            
            if start[i] != target[j]:
                return False
            if i < j and start[i] == 'L': return False
            if i > j and start[i] == 'R': return False
            i += 1
            j += 1
        
        return True

                    

