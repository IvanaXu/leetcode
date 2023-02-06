class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 数0转换为数5，有5就有2，有5*2就有0
        _r = 0
        while n:
            n //= 5
            _r += n 
        return _r
