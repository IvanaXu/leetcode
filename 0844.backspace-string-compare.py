class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        _s, _t = [], []

        for i in s:
            if i == "#":
                if _s:
                    _s.pop()
            else:
                _s.append(i)
        
        for i in t:
            if i == "#":
                if _t:
                    _t.pop()
            else:
                _t.append(i)
        
        return "".join(_s) == "".join(_t)
