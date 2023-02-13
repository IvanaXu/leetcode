class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        _maxv, _r = 0, []
        for n, v in enumerate(arr[::-1]):
            if n == 0:
                _r.append(-1)
            else:
                _r.append(_maxv)
            if v > _maxv:
                _maxv = v
        return _r[::-1]
