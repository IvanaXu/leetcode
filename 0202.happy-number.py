class Solution:
    def isHappy(self, n: int) -> bool:
        _r, _start = set(), n
        while True:
            _n = 0
            for i in str(_start):
                _n += int(i) ** 2
            
            if _n == 1:
                return True
            elif _n in _r:
                return False
            else:
                _start = _n
                _r.add(_start)
