_c = [
    ["M",   1000],
    ["D",   500],
    ["CD",  400],
    ["CM",  900],
    ["C",   100],
    ["L",   50],
    ["XL",  40],
    ["XC",  90],
    ["X",   10],
    ["V",   5],
    ["IV",  4],
    ["IX",  9],
    ["III", 3],
    ["II",  2],
    ["I",   1],
]
class Solution:
    def romanToInt(self, s: str) -> int:
        _r = 0
        while s:
            for [_k, _v] in _c:
                if s.startswith(_k):
                    s = s[len(_k):]
                    _r += _v
                    break
        return _r
