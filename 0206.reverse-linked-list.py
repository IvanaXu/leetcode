# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = []
        while head:
            h.append(head.val)
            head = head.next
        
        _r = ListNode(0)
        t = _r
        for i in h[::-1]:
            t.next = ListNode(i)
            t = t.next
        return _r.next
