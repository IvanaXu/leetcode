# Python2
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        return min([2147483647, int(dividend/float(divisor))])

# Python3
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return min([2147483647, int(dividend/divisor)])
