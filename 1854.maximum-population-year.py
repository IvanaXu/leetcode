class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        _r, _maxn, _miny = {}, 0, 2999
        for l in logs:
            for year in range(l[0], l[1]):
                _r[year] = 1 if year not in _r else _r[year]+1
        
        for _k, _v in _r.items():
            if _v > _maxn:
                _maxn = _v
                _miny = _k
            elif _v == _maxn:
                if _k < _miny:
                    _miny = _k
        return _miny
