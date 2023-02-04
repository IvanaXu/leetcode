c1 = set("-+")
c2 = set("0123456789")
_min, _max = -2147483648, 2147483647
class Solution:
    def myAtoi(self, s: str) -> int:
        _r = ""
        for i in s:
            if not _r:
                if i == " ":
                    pass
                elif i in c1|c2:
                    _r += i
                else:
                    break
            else:
                if i in c2:
                    _r += i
                else:
                    break
        try:
            _rint = int(_r)
        except:
            _rint = 0
        return min([max([_rint, _min]), _max])
