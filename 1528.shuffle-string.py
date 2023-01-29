class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        _s = list(s)
        for v, n in zip(s, indices):
            _s[n] = v
        return "".join(_s)
