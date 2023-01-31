class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        _r, _s1, _s2 = [], s1.split(" "), s2.split(" ")
        for s in _s1:
            if _s1.count(s) == 1 and s not in _s2:
                _r.append(s)
        for s in _s2:
            if _s2.count(s) == 1 and s not in _s1:
                _r.append(s)
        return _r
