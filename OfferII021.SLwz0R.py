# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        _n, _v = 0, []
        while head:
            _n += 1
            _v.append(head.val)
            head = head.next
        
        if _n == 1:
            return head
        else:
            _r = ListNode(0)
            t = _r
            for v in (_v[:_n-n]+_v[_n-n+1:]):
                t.next = ListNode(v)
                t = t.next
            return _r.next
