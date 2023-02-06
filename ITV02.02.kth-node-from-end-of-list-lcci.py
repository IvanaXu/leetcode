# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        _r = []
        while True:
            _r.append(head.val)
            head = head.next
            if not head:
                break
        return _r[-k]
