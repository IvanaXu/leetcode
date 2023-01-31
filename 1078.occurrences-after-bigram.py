class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        _r, _t = [], text.split(" ")
        _l = len(_t)
        for n, v in enumerate(_t):
            if n < _l-2 and _t[n] == first and _t[n+1] == second:
                _r.append(_t[n+2])
        return _r
