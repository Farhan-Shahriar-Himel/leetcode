class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_map = [0] * (limit + 1)
        color_freq = dict()
        res = []
        for ball, color in queries:
            if color_map[ball] != 0:
                old = color_map[ball]
                color_freq[old] -= 1
                if color_freq[old] == 0:
                    del color_freq[old]
            color_map[ball] = color
            color_freq[color] = color_freq.get(color, 0) + 1

            res.append(len(color_freq))
        
        return res
