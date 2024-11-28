# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        extra = ListNode(0, head)
        fixed, curr = extra, head
        for _ in range(left - 1):
            fixed = fixed.next
            curr = curr.next
        
        subList, preNode = curr, None
        for _ in range(right - left + 1):
            nextNode = curr.next
            curr.next = preNode
            preNode = curr
            curr = nextNode
        
        fixed.next, subList.next = preNode, curr

        return extra.next
        