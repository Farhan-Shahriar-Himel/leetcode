class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seq, visit, n = set(), set(), len(tiles)
        
        def get(wrd):
            if wrd:
                seq.add(wrd)
            for i in range(n):
                if i in visit:
                    continue
                visit.add(i)
                get(wrd + tiles[i])
                visit.remove(i)

        get("")
        
        return len(seq)
            
            