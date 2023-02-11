# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        _n, _v = 1, []
        while head:
            _v.append([
                head.val, 
                _n, 
                left if left <= _n <= right else _n,
            ])
            _n += 1
            head = head.next

        _r = ListNode(0)
        t = _r
        for v in sorted(_v, key=lambda v:(v[2], -v[1])):
            t.next = ListNode(v[0])
            t = t.next
        return _r.next
