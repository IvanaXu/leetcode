# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        _v = []
        while head:
            v = head.val
            if v not in _v:
                _v.append(v)
            head = head.next
        
        _r = ListNode(0)
        t = _r
        for v in _v:
            t.next = ListNode(v)
            t = t.next
        return _r.next
