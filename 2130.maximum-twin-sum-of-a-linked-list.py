# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        _l, _v = 0, []
        while head:
            _l += 1
            _v.append(head.val)
            head = head.next
        
        _maxv, i, j = 0, 0, _l-1
        while i < j:
            v = _v[i] + _v[j]
            if v > _maxv:
                _maxv = v
            i += 1
            j -= 1
        return _maxv
