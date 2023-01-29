class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for n in range(9, -1, -1):
            _n = str(n)*3
            if _n in num:
                return _n
        return ""
