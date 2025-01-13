class Solution:
    def minimumLength(self, s: str) -> int:
        
        def calcPartial(tmp):
            prefix = []
            mp = defaultdict(int)
            for el in tmp:
                prefix.append(mp[el] + 1)
                mp[el] += 1
            return prefix
        
        prfx = calcPartial(s)
        sfx = calcPartial(s[::-1])[::-1]

        res = len(s)
        for i in range(len(s)):
            prev = prfx[i] - 1
            nxt = sfx[i] - 1
            if prev % 2 == 1 and nxt >= 1:
                res -= 2
        
        return res

        