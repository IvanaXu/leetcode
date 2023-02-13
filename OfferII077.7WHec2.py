# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        import bisect
        _v = []
        while head:
            bisect.insort(_v, head.val)
            head = head.next

        _r = ListNode(0)
        t = _r
        for v in _v:
            t.next = ListNode(v)
            t = t.next
        return _r.next
