class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        _r, _num = 0, str(num)
        for _n in range(0, len(_num)-k+1):
            _v = int(_num[_n:_n+k])
            if _v != 0 and num%_v == 0:
                _r += 1
        return _r
