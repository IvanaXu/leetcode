class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        _r = nums[0]
        for _b in nums[1:]:
            _r = _r ^ _b
        return _r
