class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = dict()
        def isPossible(i):
            if i >= n:
                return True
            
            if i in dp:
                return dp[i]

            for w in wordDict:
                if len(w) <= n - i and w == s[i: i + len(w)]:
                    if isPossible(i + len(w)):
                        dp[i] = True
                        return True
            
            dp[i] = False
            return dp[i]
        
        return isPossible(0)
