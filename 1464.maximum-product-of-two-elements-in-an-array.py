class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        [_2, _1] = sorted(nums, reverse=True)[:2]
        return (_1- 1) * (_2-1)
