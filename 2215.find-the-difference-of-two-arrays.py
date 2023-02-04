class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        return [
            [n1 for n1 in nums1 if n1 not in nums2],
            [n2 for n2 in nums2 if n2 not in nums1],
        ]
