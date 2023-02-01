class Solution:
    def maxPower(self, s: str) -> int:
        _r = {}
        for i in s:
            _r[i] = 1 if i not in _r else _r[i]+1
        
        _max = 1
        for _k, _v in _r.items():
            for _n in range(_v, 1, -1):
                _kn = _k * _n
                
                if _kn in s:
                    if len(_kn) > _max:
                        _max = len(_kn)
                    break
        return _max
