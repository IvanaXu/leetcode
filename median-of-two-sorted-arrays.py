# https://leetcode.cn/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        if not nums:
            return 0
        nums.sort()
        l = len(nums)
        (n, m) = (l//2,l//2) if l%2 == 1 else (l//2-1,l//2)
        return (nums[n] + nums[m])/2
