# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _v = []
        while head:
            _v.append(head.val)
            head = head.next
        
        _maxl, _maxn = [], 0
        for n in _v[::-1]:
            if n >= _maxn:
                _maxn = n
                _maxl.append(_maxn)
        
        _r = ListNode(0)
        t = _r
        for v in _maxl[::-1]:
            t.next = ListNode(v)
            t = t.next
        return _r.next
