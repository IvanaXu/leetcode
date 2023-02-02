class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        _maxn, _maxv = 0, -1
        for n, v in enumerate(nums):
            if v > _maxv:
                _maxv = v
                _maxn = n
        
        for n, v in enumerate(nums):
            if n != _maxn and (_maxv < v * 2 or v == _maxv):
                return -1
        return _maxn
