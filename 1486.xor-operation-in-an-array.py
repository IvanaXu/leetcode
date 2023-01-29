class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda x,y: x^y, [start+2*i for i in range(n)])
