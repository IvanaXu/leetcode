# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        n, t = 0, head
        while t:
            if t.val == val:
                if n == 0:
                    head = t.next
                else:
                    lt.next = t.next
            lt = t
            n += 1
            t = t.next
        return head
