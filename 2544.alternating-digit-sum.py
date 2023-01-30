class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum([
            (+1 if n%2==0 else -1) * int(v) 
            for n, v in enumerate(str(n))
        ])
