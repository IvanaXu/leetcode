# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        _r = []
        while head:
            _r.append(head.val)
            head = head.next
        return _r == _r[::-1]
