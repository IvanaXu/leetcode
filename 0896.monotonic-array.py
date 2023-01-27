class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        _nums = sorted(nums)
        return nums == _nums or nums == _nums[::-1]
