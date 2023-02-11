class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        _r = 1
        for i in sorted(nums):
            if i < _r:
                pass
            elif i == _r:
                _r += 1
            else:
                return _r
        return _r
