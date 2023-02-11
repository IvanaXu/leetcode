# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        _n, _v = 0, []
        while head:
            _n += 1
            _v.append(head.val)
            head = head.next
        
        _r = ListNode(0)
        t = _r
        if _n > 0:
            k = k%_n
            _nv = _v[-k:] + _v[:-k]
            for v in _nv:
                t.next = ListNode(v)
                t = t.next
        return _r.next
