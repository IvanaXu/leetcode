# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tl1, tl2 = [], []
        while list1:
            tl1.append(list1.val)
            list1 = list1.next
        while list2:
            tl2.append(list2.val)
            list2 = list2.next
        
        _r = ListNode(0)
        t = _r
        for i in sorted(tl1 + tl2):
            t.next = ListNode(i)
            t = t.next
        return _r.next
