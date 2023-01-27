class Solution:
    def reverse(self, x: int) -> int:
        base = 1
        if x < 0:
            x = abs(x)
            base = -1
        r = base*int(str(x)[::-1])
        return r if r >= -2147483648 and r <= 2147483647 else 0
        
