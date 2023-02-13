# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tl1, tl2 = [], []
        while l1:
            tl1.append(l1.val)
            l1 = l1.next
        while l2:
            tl2.append(l2.val)
            l2 = l2.next
        cal = eval("".join(map(str, tl1))+"+"+"".join(map(str, tl2)))

        _r = ListNode(0)
        t = _r
        for v in map(int, str(cal)):
            t.next = ListNode(v)
            t = t.next
        return _r.next
