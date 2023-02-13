# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # https://leetcode.cn/problems/partition-list/
        _n, _v = 0, []
        while head:
            _v.append([_n, head.val])
            _n += 1
            head = head.next
        
        _r = ListNode(0)
        t = _r
        for v in sorted(_v, key=lambda v: v[1]>=x):
            t.next = ListNode(v[1])
            t = t.next
        return _r.next
