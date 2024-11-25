class Solution:
    def next_number(self, n):
        num = 0
        while n:
            rem = n % 10
            num += rem * rem
            n //= 10
        return num


    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.next_number(n)
            if n == 1:
                return True
        
        return False