from collections import defaultdict as dd, deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        adj = dd(list)
        def isNext(s1, s2):
            on = False
            for i in range(8):
                if s1[i] != s2[i]:
                    if on:
                        return False
                    on = True
            return True
        
        for mutations in bank:
            if isNext(startGene, mutations):
                adj[startGene].append(mutations)
        
        for i in range(len(bank)):
            for j in range(len(bank)):
                if i == j:
                    continue
                if isNext(bank[i], bank[j]):
                    adj[bank[i]].append(bank[j])
                    adj[bank[j]].append(bank[i])
        
        def bfs(src):
            q = deque()
            q.append([src, 0])
            seen = set()
            while q:
                now, level = q.popleft()
                if now == endGene:
                    return level
                for nxt in adj[now]:
                    if nxt not in seen:
                        q.append([nxt, level + 1])
                        seen.add(nxt)
            
            return -1

        return bfs(startGene)
        
