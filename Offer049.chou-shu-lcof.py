class Solution:
    def nthUglyNumber(self, n: int) -> int:
        _r, p2, p3, p5 = [1], 0, 0, 0
        for _ in range(n-1):
            v2, v3, v5 = _r[p2]*2, _r[p3]*3, _r[p5]*5
            _r.append(min([v2, v3, v5]))

            p2 += _r[-1]==v2
            p3 += _r[-1]==v3
            p5 += _r[-1]==v5
        return _r[-1]
