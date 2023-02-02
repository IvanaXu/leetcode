# Python2
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [bin(i).count("1") for i in range(n+1)]

# Python3
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [f"{i:b}".count("1") for i in range(n+1)]

