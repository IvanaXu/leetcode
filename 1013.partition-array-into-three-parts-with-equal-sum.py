# Python2
class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        _sum = sum(arr)
        _r, _n = 0, 0
        for v in arr:
            _r += v
            if _r == _sum/3.0:
                _r = 0
                _n += 1
        return _n >= 3

# Python3
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        _sum = sum(arr)
        _r, _n = 0, 0
        for v in arr:
            _r += v
            if _r == _sum/3:
                _r = 0
                _n += 1
        return _n >= 3
