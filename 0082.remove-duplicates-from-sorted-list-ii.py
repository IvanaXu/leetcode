# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t1, t2 = [], set()
        while head:
            v = head.val
            if v not in t1:
                t1.append(v)
            else:
                t2.add(v)
            head = head.next
        
        _r = ListNode(0)
        t = _r
        for i in t1:
            if i not in t2:
                t.next = ListNode(i)
                t = t.next
        return _r.next
