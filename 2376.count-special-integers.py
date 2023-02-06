def fcnt(cnt):
    _r = 0
    _cnt = 0 if cnt == 0 else len(str(cnt))
    for c in range(_cnt+1):
        if c == 0:
            _r = 0
        elif c == 1:
            _r = 9
        elif c == 2:
            _r = 90
        else:
            res = 9
            num = 9
            for _ in range(2, c+1):
                res *= num
                num -= 1
            _r += res
    return _r
# print(fcnt(0), 0)
# print(fcnt(9), 9)
# print(fcnt(99), 90)
# print(fcnt(999), 738)
# print(fcnt(9999), 5274)

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        _l = len(str(n))
        _min, _max = 10**(_l-1)-1, 10**_l-1 
        
        if (n-_min) > (_max-n):
            _r = fcnt(_max)
            # print(1, _max, _r)
            for _n in range(_max, n, -1):
                _sn = str(_n)
                if _n > 0 and len(_sn) == len(set(_sn)):
                    _r -= 1
            return _r
        else:
            _r = fcnt(_min)
            # print(2, _min, _r)
            for _n in range(_min+1, n+1, 1):
                _sn = str(_n)
                if _n > 0 and len(_sn) == len(set(_sn)):
                    _r += 1
            return _r




