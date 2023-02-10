# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        _r = []
        while head:
            _r.append(head.val)
            head = head.next
        return _r == _r[::-1]
