class Solution:
    def repeatedCharacter(self, s: str) -> str:
        _r = set()
        for i in s:
            if i not in _r:
                _r.add(i)
            else:
                return i
