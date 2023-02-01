class Solution:
    def numberOfMatches(self, n: int) -> int:
        c = 0
        while True:
            if n%2 == 0:
                _n = n//2
                n = _n
                c += _n
            else:
                _n = (n-1)//2
                n = _n + 1
                c += _n
            
            if n == 1:
                break
        return c
