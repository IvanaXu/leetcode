# Python2
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        import copy
        _n = 0
        for n, v in enumerate(copy.copy(arr)):
            if v == 0:
                arr.insert(n+_n, 0)
                arr.pop(-1)
                _n += 1

# Python3
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        _n = 0
        for n, v in enumerate(arr.copy()):
            if v == 0:
                arr.insert(n+_n, 0)
                arr.pop(-1)
                _n += 1
