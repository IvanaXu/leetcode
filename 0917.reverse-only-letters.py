cC = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        _r, _s = "", "".join([i for i in s if i in cC][::-1])
        _l, _n = len(s), 0

        for n in range(_l):
            if s[n] in cC:
                _r += _s[n-_n]
            else:
                _r += s[n]
                _n += 1
        return _r
