c = "abcdefghijklmnopqrstuvwxyz"
class Solution:
    def replaceDigits(self, s: str) -> str:
        _l, _s = len(s), ""
        for i in range(_l):
            if s[i] in c:
                if i < _l-1:
                    [n1, n2] = list(s[i:i+2])
                    _s += f"{n1}{c[c.index(n1)+int(n2)]}"
                else:
                    _s += s[i]
        return _s
