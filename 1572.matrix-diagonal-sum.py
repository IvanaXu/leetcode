class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        _r, _l = {}, len(mat)
        for n in range(_l):
            _r[(n ,n)] = mat[n][n]
            _r[(_l-n-1, n)] = mat[_l-n-1][n]
        return sum(_r.values())
