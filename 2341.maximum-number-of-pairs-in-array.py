class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        _r = {}
        for i in nums:
            _r[i] = 1 if i not in _r else _r[i]+1
        _1, _2 = 0, 0
        for _v in _r.values():
            _1 += _v//2
            _2 += _v%2
        return [_1, _2]
