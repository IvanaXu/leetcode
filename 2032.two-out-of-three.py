class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        _nums1, _nums2, _nums3 = set(nums1), set(nums2), set(nums3)
        return list((_nums1&_nums2)|(_nums1&_nums3)|(_nums2&_nums3))
