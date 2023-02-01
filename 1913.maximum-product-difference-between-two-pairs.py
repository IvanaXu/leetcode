class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        _nums = sorted(nums)
        return (_nums[-1] * _nums[-2]) - (_nums[0] * _nums[1])
