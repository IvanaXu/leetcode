class Solution:
    def convertToBase7(self, num: int) -> str:
        N = 7

        _r = ""
        _f, _n = "-" if num < 0 else "", -num if num < 0 else num
        while True:
            s = _n//N
            y = _n%N
            _r += str(y)

            if s == 0:
                break
            else:
                _n = s
        return _f + _r[::-1]

