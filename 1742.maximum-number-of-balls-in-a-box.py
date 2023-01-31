class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        _r, _max = {}, 0
        for i in range(lowLimit, highLimit+1):
            _box = sum([int(j) for j in str(i)])
            if _box not in _r:
                _r[_box] = 1
            else:
                _r[_box] += 1
            
            if _r[_box] > _max:
                _max = _r[_box]
        return _max
