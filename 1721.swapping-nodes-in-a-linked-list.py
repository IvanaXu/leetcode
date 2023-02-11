# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        _n, _v = 0, []
        while head:
            _v.append([head.val, _n])
            head = head.next
        _v[k-1], _v[-k] = _v[-k], _v[k-1]
        
        _r = ListNode(0)
        t = _r
        for v in _v:
            t.next = ListNode(v[0])
            t = t.next
        return _r.next
