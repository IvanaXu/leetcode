class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        _maxr = {}
        for d in demand:
            _r = {}
            for i in d:
                _r[i] = 1 if i not in _r else _r[i]+1
            
            for _k, _v in _r.items():
                _maxr[_k] = _v if _k not in _maxr else max([_v, _maxr[_k]])
        return sum(_maxr.values())
