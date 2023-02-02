class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        _nums1 = sorted(nums, reverse=True)
        _nums2 = _nums1[::-1]
        for n in _nums1:
            if -n in _nums2:
                return n
        return -1
