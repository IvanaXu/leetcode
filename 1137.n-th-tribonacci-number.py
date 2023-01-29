class Solution:
    def tribonacci(self, n: int) -> int:
        _r = 1

        if n == 0:
            _r = 0
        elif n == 1:
            _r = 1
        elif n == 2:
            _r = 1
        else:
            _1, _2, _3 = 0, 0, 1
            for i in range(3, n+1):
                _1 = _2
                _2 = _3
                _3 = _r
                _r = _1 + _2 + _3
        return _r
