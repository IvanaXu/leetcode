# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        _r = []
        while head:
            _r.append(head.val)
            head = head.next
        return int("".join(map(str, _r)), 2)
