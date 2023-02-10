# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tid = {}
        hA, hB = headA, headB
        while hA:
            # 节点地址是否一致
            tid[id(hA)] = hA.val
            hA = hA.next
        
        while hB:
            if id(hB) in tid:
                return ListNode(hB.val)
            hB = hB.next
