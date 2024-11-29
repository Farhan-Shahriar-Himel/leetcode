# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
            
        curr = head
        leftListHead = ListNode()
        leftList = leftListHead
        rightListHead = ListNode()
        rightList = rightListHead

        while curr:
            if curr.val < x:
                leftList.next = ListNode(curr.val)
                leftList = leftList.next
            else:
                rightList.next = ListNode(curr.val)
                rightList = rightList.next
            curr = curr.next
        
        curr = leftListHead
        while curr.next:
            curr = curr.next
        
        curr.next = rightListHead.next

        return leftListHead.next