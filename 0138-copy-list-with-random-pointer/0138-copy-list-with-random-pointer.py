"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return head

        mp = dict()
        tmp = head
        while tmp:
            mp[tmp] = Node(tmp.val)
            tmp = tmp.next
        
        new = head
        while new:
            mp[new].next = mp.get(new.next)
            mp[new].random = mp.get(new.random)
            new = new.next
        
        return mp[head]


        