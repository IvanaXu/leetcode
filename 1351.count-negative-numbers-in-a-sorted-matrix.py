class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        _n = 0
        for _grid in grid:
            for g in _grid[::-1]:
                if g < 0:
                    _n += 1
                else:
                    break
        return _n
