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
