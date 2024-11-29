# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        def get_size():
            curr = head
            cnt = 0
            while curr:
                curr = curr.next
                cnt += 1
            return cnt
        
        size = get_size()
        k %= size
        k = size - k
        if k == 0:
            return head
        
        curr = head
        nextHead = None
        for _ in range(k - 1):
            curr = curr.next
        
        nextHead = curr.next
        curr.next = None

        newCurr = nextHead
        while newCurr.next:
            newCurr = newCurr.next
        
        newCurr.next = head

        return nextHead
