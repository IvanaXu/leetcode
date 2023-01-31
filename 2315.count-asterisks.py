class Solution:
    def countAsterisks(self, s: str) -> int:
        _r = 0
        for n, v in enumerate(s.split("|")):
            if n%2 == 1:
                pass
            else:
                _r += v.count("*")
        return _r
