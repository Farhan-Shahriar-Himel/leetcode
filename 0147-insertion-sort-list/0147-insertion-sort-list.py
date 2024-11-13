# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        key = head
        while key:
            next_node = key.next
            if not new_head or key.val <= new_head.val:
                key.next = new_head
                new_head = key
            else:
                curr = new_head
                while curr.next and curr.next.val < key.val:
                    curr = curr.next
                key.next = curr.next
                curr.next = key
            
            key = next_node
        
        return new_head