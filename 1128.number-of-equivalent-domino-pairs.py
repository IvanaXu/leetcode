class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        _r = {}
        for d in dominoes:
            d1, d2 = tuple(d), tuple(d[::-1])
            _d = d1 if d1 < d2 else d2
            _r[_d] = 1 if _d not in _r else _r[_d]+1
        return sum([_v*(_v-1)//2 for _v in _r.values()])
