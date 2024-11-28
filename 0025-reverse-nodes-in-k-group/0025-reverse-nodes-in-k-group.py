# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head and k == 1:
            return head
        
        def get_size():
            curr = head
            cnt = 0
            while curr:
                curr = curr.next
                cnt += 1
            return cnt

        def show(head):
            tmp = head
            while tmp:
                print(tmp.val, end="->")
                tmp = tmp.next
            print()

        
        size = get_size()
        extra = ListNode(0, head)
        curr = head
        connect = extra

        while size >= k:
            preNode = None
            subList = curr
            # print(preNode, subList.val, curr.val)
            for _ in range(k):
                nextNode = curr.next
                curr.next = preNode
                preNode = curr
                curr = nextNode
            
            subList.next = curr
            connect.next = preNode
            connect = subList
            size -= k
        
        return extra.next
            

        