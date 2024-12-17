# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a = []
        for head in lists:
            while head:
                a.append(head.val)
                head = head.next
        
        a.sort()

        new = ListNode(0)
        tmp = new

        for num in a:
            tmp.next = ListNode(num)
            tmp = tmp.next
        
        return new.next
        