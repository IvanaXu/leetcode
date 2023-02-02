class Solution:
    def minimumSum(self, num: int) -> int:
        _n = sorted(str(num))
        return sum([int(f"{_n[0]}{_n[2]}"), int(f"{_n[1]}{_n[3]}")])
