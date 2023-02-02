class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        _r = {}
        for i in arr:
            _r[i] = 1 if i not in _r else _r[i]+1
        return len(set(_r.keys())) == len(set(_r.values()))
