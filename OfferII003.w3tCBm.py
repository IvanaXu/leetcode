# Python2
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [bin(_n).count("1") for _n in range(0, n+1)]

# Python3
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [f"{_n:b}".count("1") for _n in range(0, n+1)]

