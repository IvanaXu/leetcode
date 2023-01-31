class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        _maxn, _maxr = 0, "a"
        for n, r in enumerate(releaseTimes):
            _n, _r = r if n == 0 else r-releaseTimes[n-1], keysPressed[n]
            if (_n > _maxn) or (_n == _maxn and _r >= _maxr):
                _maxn, _maxr = _n, _r
        return _maxr
