# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def merge(self, left, right):
        new = ListNode()
        tmp = new
        while left and right:
            if left.val < right.val:
                tmp.next = left
                tmp = tmp.next
                left = left.next
            else:
                tmp.next = right
                tmp = tmp.next
                right = right.next
            
        if left:
            tmp.next = left
        if right:
            tmp.next = right
            
        return new.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        back = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(back)
        
        return self.merge(left, right)
    