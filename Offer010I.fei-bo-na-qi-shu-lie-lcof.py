class Solution:
    def fib(self, n: int) -> int:
        M = 1000000007
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for i in range(2, n+1):
                c = (a+b)%M
                a = b
                b = c
            return c
