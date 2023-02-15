class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        _l, _minn, _minv, _maxn, _maxv = 0, 0, 999999, 0, -999999
        for n, v in enumerate(nums):
            _l += 1

            if v < _minv:
                _minn = n
                _minv = v
            
            if v > _maxv:
                _maxn = n
                _maxv = v
        # 
        _minn1 = _minn+1
        _minn2 = _l-_minn
        _maxn1 = _maxn+1
        _maxn2 = _l-_maxn
        return min([
            max([_minn1, _maxn1]),
            _minn1 + _maxn2,
            max([_minn2, _maxn2]),
            _minn2 + _maxn1,
        ])
