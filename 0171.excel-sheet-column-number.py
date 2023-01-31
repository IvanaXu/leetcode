C = {
    c: n+1 
    for n, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
}
N = 26

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        _r = 0
        for n, c in enumerate(columnTitle[::-1]):
            _r += N ** n * C.get(c)
        return _r
