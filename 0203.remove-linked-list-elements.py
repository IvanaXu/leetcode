# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        _r = ListNode(0)
        t = _r
        while head:
            v = head.val
            if v != val:
                t.next = ListNode(v)
                t = t.next
            head = head.next
        return _r.next
