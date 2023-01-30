class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        
        _sum = sum([i for i in range(1, n+1)])
        _st, _ed = _sum, 0

        for i in range(n, 1, -1):
            _ed += i
            if _st == _ed:
                return i
            elif _ed > _st:
                return -1
            
            _st -= i
        return -1
