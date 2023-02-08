class Solution:
    def waysToStep(self, n: int) -> int:
        # 斐波拉契
        # 1/1, 2/2, 3/4, 4/7, 5/13, 6/24
        # 6/24 = (5/13 + 1) or (4/7 + 2) or(3/4 + 3)
        M = 1000000007
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            a, b, c, d = 1, 2, 4, 0
            for i in range(4, n+1):
                d = (a+b+c)%M
                a = b
                b = c
                c = d
            return d
