class Solution:
    def arrangeCoins(self, n: int) -> int:
        # _st 根据(1+x)*x/2数列公式倒推导近似初始值
        _st = int(math.sqrt(2*n))-1
        gnum = lambda x: (1+x)*x/2
        for i in range(_st, n+1):
            print(i)
            if gnum(i) <= n < gnum(i+1):
                return i
