class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        _min, _max = min([a, b]), max([a, b])
        return len([
            i for i in range(1, _min+1)
            if _max%i == 0 and _min%i == 0
        ])
