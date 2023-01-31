class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        _l = len(s)
        for n in range(1, _l):
            _s = s[:n]
            if _s * (_l//len(_s)) == s:
                return True
        return False
