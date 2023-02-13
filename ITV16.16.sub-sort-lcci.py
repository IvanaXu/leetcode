class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        _min, _max, _array = 9999999, -1, sorted(array)
        
        _n = 0
        for i, j in zip(array, _array):
            if i != j and _n < _min:
                _min = _n
                break
            _n += 1
        
        _n = len(array) - 1
        for i, j in zip(array[::-1], _array[::-1]):
            if i != j and _n > _max:
                _max = _n
                break
            _n -= 1
        
        return [
            -1 if _min == 9999999 else _min,
            -1 if _max == -1 else _max
        ]
