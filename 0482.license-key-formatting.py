class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace("-", "")[::-1]
        _s = ""
        for n, v in enumerate(s):
            _s += v
            if (n+1)%k == 0:
                _s += "-"
        return _s[::-1].strip("-")
