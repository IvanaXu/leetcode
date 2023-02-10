# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        _v = []
        while head:
            v = id(head.next)
            if v not in _v:
                _v.append(v)
            else:
                return True
            head = head.next
        return False
