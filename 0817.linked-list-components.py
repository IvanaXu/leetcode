# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        # 返回列表 nums 中组件的个数
        _r, _k = "", 0
        while head:
            v = head.val
            if v in nums:
                _k = "O"
            else:
                _k = "/"
            _r += _k
            head = head.next
        return sum(["O" in i for i in _r.split("/")])
