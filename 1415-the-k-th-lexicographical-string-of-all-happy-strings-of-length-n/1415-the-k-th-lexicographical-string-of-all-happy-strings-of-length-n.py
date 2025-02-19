class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        
        def make(s):
            if len(res) == k:
                return
            if len(s) == n:
                res.append(s)
            if len(s) > n:
                return
            
            if not s or s[-1] != 'a':
                make(s + 'a')
            if not s or s[-1] != 'b':
                make(s + 'b')
            if not s or s[-1] != 'c':
                make(s + 'c')

        make("")
        
        return res[-1] if len(res) == k else ""
            
            

            
