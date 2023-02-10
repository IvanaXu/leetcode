# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tl1, tl2 = [], []
        while l1:
            tl1.append(l1.val)
            l1 = l1.next
        while l2:
            tl2.append(l2.val)
            l2 = l2.next
        
        _r = ListNode(0)
        t = _r
        for i in sorted(tl1 + tl2):
            t.next = ListNode(i)
            t = t.next
        return _r.next
