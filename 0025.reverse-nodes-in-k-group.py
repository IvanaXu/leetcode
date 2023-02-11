# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        _n, _v = 0, []
        while head:
            _n += 1
            _v.append(head.val)
            head = head.next
        
        _g, _r = _n//k, ListNode(0)
        t = _r
        for i in range(_g+1):
            _left, _right = i*k, (i+1)*k
            _nv = _v[_left:_right][::-1] if _right <= _n else _v[_left:_right]
            
            for v in _nv:
                t.next = ListNode(v)
                t = t.next
        return _r.next
