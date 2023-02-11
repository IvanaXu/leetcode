# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        _n, _v, _t = 0, [], head
        while _t:
            _v.append(_t.val)
            _n += 1
            _t = _t.next
        
        t = head
        i, j = 0, _n-1
        while i <= j:
            # print(_v[i], _v[j])
            if i == 0:
                pass
            else:
                t.next = ListNode(_v[i])
                t = t.next
            if i < j:
                t.next = ListNode(_v[j])
                t = t.next
            i += 1
            j -= 1
