class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        """
        三个指针（p3,p5,p7)分别代表3，5，7乘某个数所能贡献的最小值(val)，
        当这个val被用过了，就不会再出现，因此需要将对应的指针位置+1
        """
        _r, p3, p5, p7 = [1], 0, 0, 0
        for _ in range(k-1):
            v3, v5, v7 = _r[p3]*3, _r[p5]*5, _r[p7]*7
            _r.append(min([v3, v5, v7]))
            
            p3 += _r[-1]==v3
            p5 += _r[-1]==v5
            p7 += _r[-1]==v7
        return _r[-1]
