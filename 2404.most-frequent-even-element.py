class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        _r = {}
        for n in nums:
            if n%2 == 0:
                _r[n] = 1 if n not in _r else _r[n]+1
        
        if len(_r) == 0:
            return -1
        else:
            _max = max(_r.values())
            return min([_k for _k, _v in _r.items() if _v == _max])
