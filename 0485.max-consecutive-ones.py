class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        _max, _n = 0, 0
        for v in nums:
            _n = _n + 1 if v == 1 else 0

            if _n > _max:
                _max = _n
        return _max
