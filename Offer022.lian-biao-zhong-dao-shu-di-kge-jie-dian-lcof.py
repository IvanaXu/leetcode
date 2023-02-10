# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        _n, _r = 0, {}
        while head:
            _r[_n] = head
            _n += 1
            head = head.next
        return _r[_n-k]
