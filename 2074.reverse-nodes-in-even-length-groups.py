# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _n, _v = 0, []
        while head:
            _n += 1
            _v.append(head.val)
            head = head.next
        
        _nv, _i, _g = [], 0, 1
        while True:
            if _i+_g < _n:
                _nv.extend(_v[_i:_i+_g][::-1] if _g%2 == 0 else _v[_i:_i+_g])
            else:
                _nv.extend(_v[_i:_n][::-1] if (_n-_i)%2 == 0 else _v[_i:_n])
                break
            _i += _g
            _g += 1
        
        _r = ListNode(0)
        t = _r
        for v in _nv:
            t.next = ListNode(v)
            t = t.next
        return _r.next
