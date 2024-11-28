# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_size():
            curr = head
            cnt = 0
            while curr:
                curr = curr.next
                cnt += 1
            return cnt

        dummy = ListNode(0, head)
        size = get_size()
        ind = size - n
        curr = dummy
        for _ in range(ind):
            curr = curr.next
        
        curr.next = curr.next.next
        return dummy.next