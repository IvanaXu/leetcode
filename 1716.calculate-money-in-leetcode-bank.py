class Solution:
    def totalMoney(self, n: int) -> int:
        N = 7
        _r, _i = 0, 0
        for i in range(1, n+1):
            if i%N == 1:
                _i = i//N+1
                _r += _i
            else:
                _i += 1
                _r += _i
        return _r
