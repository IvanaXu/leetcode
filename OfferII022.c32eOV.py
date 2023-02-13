# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        _v = []
        while head:
            v = id(head)
            # print(v, head.val)
            if v not in _v:
                _v.append(v)
            else:
                return head
            head = head.next
