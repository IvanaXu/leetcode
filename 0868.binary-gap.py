# Python2
class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        _st, _max = -1, 0
        for nb, vb in enumerate(bin(n).replace("0b","")):
            if vb == "1":
                if _st == -1:
                    _st = nb
                else:
                    maxb = nb - _st
                    if maxb > _max:
                        _max = maxb
                    _st = nb
        return _max

# Python3
class Solution:
    def binaryGap(self, n: int) -> int:
        _st, _max = -1, 0
        for nb, vb in enumerate(f"{n:b}"):
            if vb == "1":
                if _st == -1:
                    _st = nb
                else:
                    maxb = nb - _st
                    if maxb > _max:
                        _max = maxb
                    _st = nb
        return _max
