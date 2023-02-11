# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _r = ListNode(0)
        v, t = 0, _r

        while head:
            iv = head.val
            v += iv
            if iv == 0:
                if v == 0:
                    pass
                else:
                    t.next = ListNode(v)
                    t = t.next
                    v = 0
            head = head.next
        return _r.next
