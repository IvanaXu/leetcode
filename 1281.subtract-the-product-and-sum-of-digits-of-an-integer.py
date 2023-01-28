class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ln = [int(i) for i in str(n)]
        return reduce(lambda x, y: x*y, ln) - reduce(lambda x, y: x+y, ln)
