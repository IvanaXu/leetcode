# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
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
