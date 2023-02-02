class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        _k, _r1, _r2 = set(), {}, {}
        for w in word1:
            _k.add(w)
            _r1[w] = 1 if w not in _r1 else _r1[w]+1
        for w in word2:
            _k.add(w)
            _r2[w] = 1 if w not in _r2 else _r2[w]+1
        
        for k in _k:
            if abs(_r1.get(k, 0) - _r2.get(k, 0)) > 3:
                return False
        return True
