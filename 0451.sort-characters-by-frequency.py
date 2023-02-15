class Solution:
    def frequencySort(self, s: str) -> str:
        _r = {}
        for i in s:
            _r[i] = 1 if i not in _r else _r[i] + 1
        return "".join([i[0]*i[1] for i in sorted(_r.items(), key=lambda x: x[1], reverse=True)])
