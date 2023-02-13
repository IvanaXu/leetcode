class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        _n, _r = 0, {}
        for v in arr:
            if v not in _r:
                _r[v] = 1
            else:
                _r[v] += 1
            _n += 1
        
        for _k, _v in _r.items():
            if _v > _n/4:
                return _k
