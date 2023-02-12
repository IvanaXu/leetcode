# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import bisect
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tl = []
        for ilist in lists:
            while ilist:
                bisect.insort(tl, ilist.val)
                ilist = ilist.next
        
        _r = ListNode(0)
        t = _r
        for i in tl:
            t.next = ListNode(i)
            t = t.next
        return _r.next
