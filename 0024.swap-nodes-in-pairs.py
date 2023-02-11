# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _l, _v = 0, []
        while head:
            _l += 1
            _v.append(head.val)
            head = head.next
        
        _nv = []
        for i in range(0, _l, 2):
            _nv.extend(_v[i:i+2][::-1])
        
        _r = ListNode(0)
        t = _r
        for v in _nv:
            t.next = ListNode(v)
            t = t.next
        return _r.next
