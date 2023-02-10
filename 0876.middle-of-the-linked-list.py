# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t, _n, _r = head, 0, {}
        while t:
            _n += 1
            _r[_n] = t.next
            t = t.next
        return head if _n == 1 else _r[_n//2]
