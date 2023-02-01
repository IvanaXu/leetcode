class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        else:
            _n, _s1, _s2 = 0, [], []
            for _1, _2 in zip(s1, s2):
                if _1 != _2:
                    _s1.append(_1)
                    _s2.append(_2)
                    _n += 1
            return _n == 2 and _s1 == _s2[::-1]
