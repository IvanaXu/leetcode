class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        _r = set(nums1) & set(nums2)
        return min(_r) if _r else -1
