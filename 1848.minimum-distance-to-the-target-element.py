class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        _minc = 99999
        for n, v in enumerate(nums):
            if v == target:
                c = abs(n - start)
                if c < _minc:
                    _minc = c
        return _minc
