c = "abcdefghijklmnopqrstuvwxyz"
class Solution:
    def freqAlphabets(self, s: str) -> str:
        _r, _l = [], len(s)
        for n in range(_l):
            if n < _l-2 and s[n+2] == "#":
                _r.append(s[n:n+2])
            elif (s[n] == "#") or (n < _l-1 and s[n+1] == "#"):
                pass
            else:
                 _r.append(s[n])
        return "".join([c[int(i)-1] for i in _r])
