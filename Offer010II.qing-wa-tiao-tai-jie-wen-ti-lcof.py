class Solution:
    def numWays(self, n: int) -> int:
        M = 1000000007
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            a, b = 2, 3
            for i in range(4, n+1):
                _r = a + b
                a = b
                b = _r
            return b%M
