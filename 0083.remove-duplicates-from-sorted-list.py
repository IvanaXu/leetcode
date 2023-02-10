# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _r, _v, lv = ListNode(0), [], 999
        t = _r
        while head:
            v = head.val
            if v != lv:
                t.next = ListNode(v)
                t = t.next
            lv = v
            head = head.next
        return _r.next
