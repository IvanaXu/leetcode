class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        
        _ps, _sp = {}, {}
        for _p, _s in zip(pattern, s):
            if _p not in _ps:
                _ps[_p] = _s
            elif _ps[_p] != _s:
                return False
            
            if _s not in _sp:
                _sp[_s] = _p
            elif _sp[_s] != _p:
                return False
        return True
