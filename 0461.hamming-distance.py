# Python2
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count("1")

# Python3
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return f"{x^y:b}".count("1")
