# Python2
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")

# Python3
class Solution:
    def hammingWeight(self, n: int) -> int:
        return f"{n:b}".count("1")
