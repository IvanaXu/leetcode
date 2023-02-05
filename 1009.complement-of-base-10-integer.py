# Python2
class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 5 > 2, 101^111 = 010 = 2
        return n ^ (2**(len(bin(n))-2)-1)

# Python3
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # 5 > 2, 101^111 = 010 = 2
        return n ^ (2**len(f"{n:b}")-1)
