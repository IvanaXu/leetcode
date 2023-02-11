class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # 1 <= n <= 100, 质数数量! * 非质数数量!
        M = 1000000007
        C = [
            2, 3, 5, 7, 11, 
            13, 17, 19, 23, 29, 
            31, 37, 41, 43, 47, 
            53, 59, 61, 67, 71, 
            73, 79, 83, 89, 97
        ]
        if n == 1:
            return 1
        _n1 = sum([c <= n for c in C])
        _fn = lambda x, y: x*y
        _r = reduce(_fn, range(1, _n1+1))%M * reduce(_fn, range(1, n-_n1+1))%M
        return _r
