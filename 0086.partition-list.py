# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        _n, _v = 0, []
        while head:
            _v.append([_n, head.val])
            _n += 1
            head = head.next
        
        _r = ListNode(0)
        t = _r
        for v in sorted(_v, key=lambda v: v[1]<x, reverse=True):
            t.next = ListNode(v[1])
            t = t.next
        return _r.next
