class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return min([2147483647, int(dividend/divisor)])
