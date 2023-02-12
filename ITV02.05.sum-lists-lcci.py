# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tl1, tl2 = [], []
        while l1:
            tl1.append(str(l1.val))
            l1 = l1.next
        while l2:
            tl2.append(str(l2.val))
            l2 = l2.next
        v = str(int("".join(tl1[::-1])) + int("".join(tl2[::-1])))[::-1]
        
        _r = ListNode(0)
        t = _r
        for i in v:
            t.next = ListNode(int(i))
            t = t.next
        return _r.next
