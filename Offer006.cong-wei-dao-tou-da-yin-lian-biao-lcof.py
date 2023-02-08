# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        _r = []
        while True:
            if not head:
                return _r[::-1]
            _r.append(head.val)
            head = head.next
