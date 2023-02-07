# Python2
class Solution(object):
    def insertBits(self, N, M, i, j):
        """
        :type N: int
        :type M: int
        :type i: int
        :type j: int
        :rtype: int
        """
        _gap = j+1-i
        _0 = ["0"]*_gap
        _r = (_0+list(bin(N).replace("0b","")))[::-1]
        _M = (_0+list(bin(M).replace("0b","")))[-_gap:][::-1]
        _r[i:j+1] = _M
        return int("".join(_r[::-1]), 2)

# Python3
class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        _gap = j+1-i
        _0 = ["0"]*_gap
        _r = (_0+list(f"{N:b}"))[::-1]
        _M = (_0+list(f"{M:b}"))[-_gap:][::-1]
        _r[i:j+1] = _M
        return int("".join(_r[::-1]), 2)
