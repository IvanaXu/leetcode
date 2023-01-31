class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        _r = {}
        for i in s:
            if i not in _r:
                _r[i] = 1
            else:
                _r[i] += 1
        return len(set(_r.values())) == 1
