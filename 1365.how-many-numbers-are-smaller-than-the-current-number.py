class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        _nums = sorted(nums)
        return [_nums.index(i) for i in nums]class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        _nums = sorted(nums)
        return [_nums.index(i) for i in nums]
