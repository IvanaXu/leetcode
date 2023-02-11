# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import bisect
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tl = []
        while list1:
            bisect.insort(tl, list1.val)
            list1 = list1.next
        while list2:
            bisect.insort(tl, list2.val)
            list2 = list2.next
        
        _r = ListNode(0)
        t = _r
        for i in tl:
            t.next = ListNode(i)
            t = t.next
        return _r.next
