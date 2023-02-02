class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        _t, _minid, _maxt = 0, n, 0
        for l in logs:
            [lid, it] = l
            uset = it - _t
            _t = it

            if uset > _maxt:
                _maxt, _minid = uset, lid
            elif uset == _maxt and lid < _minid:
                _minid = lid
        return _minid
