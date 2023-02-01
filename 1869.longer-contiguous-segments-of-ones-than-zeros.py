class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        _l, _0, _1 = len(s), 0, 0
        for n in range(_l, 0, -1):
            if n * "0" in s:
                _0 = n
                break
        
        for n in range(_l, 0, -1):
            if n * "1" in s:
                _1 = n
                break
        
        return _1 > _0
