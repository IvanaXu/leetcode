class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        _r = {}
        for i in s:
            _r[i] = 1 if i not in _r else _r[i]+1
        return sum([_v%2 == 1 for _v in _r.values()]) <= 1
