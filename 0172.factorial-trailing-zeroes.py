class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        (7) 30
        (6) 5 10 15 20 25 30
        (1) 25 = 5*5, +1
        每间隔 5 个数有一个数可以被 5 整除, 
        然后在这些可被 5 整除的数中, 每间隔 5 个数又有一个可以被 25 整除
        ...
        """
        _r = 0
        while n >= 5:
            _r += n//5
            n //= 5
        return _r
