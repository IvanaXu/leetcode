class Solution:
    def fib(self, n: int) -> int:
        # def _fib(n):
        #     d = {
        #         0: 0,
        #         1: 1,
        #     }
        #     if n in d:
        #         return d[n]
        #     return _fib(n-1) + _fib(n-2)
        # return _fib(n)

        # 用黄金比例来计算斐波那契数
        u = 1.618034
        return int((u**n - (1-u)**n)/(5**0.5))

