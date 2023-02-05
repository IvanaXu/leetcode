# Python2
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 5 > 2, 101^111 = 010 = 2
        return num ^ (2**(len(bin(num))-2)-1)

# Python3
class Solution:
    def findComplement(self, num: int) -> int:
        # 5 > 2, 101^111 = 010 = 2
        return num ^ (2**len(f"{num:b}")-1)
