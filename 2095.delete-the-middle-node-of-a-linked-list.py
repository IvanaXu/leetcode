# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t, _n = head, 0
        while t:
            _n += 1
            t = t.next
        
        if _n == 1:
            return head.next
        else:
            t, _m = head, 0
            while t:
                if _m == _n//2-1:
                    t.next = t.next.next if t.next else t.next
                _m += 1
                t = t.next
            return head
