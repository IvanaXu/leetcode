class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        _l = len(s)
        _g, _m = _l//k, _l%k
        if _m > 0:
            _g += 1
            s = s + (k-_m) * fill
        return [s[n*k:(n+1)*k] for n in range(_g)]
