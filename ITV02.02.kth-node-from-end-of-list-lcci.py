# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        _r = []
        while True:
            _r.append(head.val)
            head = head.next
            if not head:
                break
        return _r[-k]
