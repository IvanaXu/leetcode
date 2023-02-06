class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        _r = 0
        for i in range(1, income+1):
            for [bv0, bv1] in brackets:
                if i <= bv0:
                    _r += bv1/100
                    break
        return _r
