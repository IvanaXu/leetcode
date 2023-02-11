# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        _r, _n = ListNode(0), 0
        t = _r

        while list1:
            if a <= _n <= b:
                while list2:
                    t.next = ListNode(list2.val)
                    t = t.next
                    list2 = list2.next
            else:
                t.next = ListNode(list1.val)
                t = t.next
            _n += 1
            list1 = list1.next
        return _r.next
