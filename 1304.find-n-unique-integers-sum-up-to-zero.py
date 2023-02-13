class Solution:
    def sumZero(self, n: int) -> List[int]:
        _r = [] if n%2 == 0 else [0]
        for i in range(1, n//2+1):
            _r.extend([i, -i])
        return _r
