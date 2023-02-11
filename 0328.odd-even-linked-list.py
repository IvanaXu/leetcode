# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _n, _v = 0, []
        while head:
            _v.append([head.val, _n])
            _n += 1
            head = head.next
        
        _r = ListNode(0)
        t = _r
        for v in sorted(_v, key=lambda x: (x[1]%2, x[1])):
            t.next = ListNode(v[0])
            t = t.next
        return _r.next
