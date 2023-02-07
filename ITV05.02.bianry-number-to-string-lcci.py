class Solution:
    def printBin(self, num: float) -> str:
        _r = ["0", "."]
        for i in range(32):
            if num == 0:
                return "".join(_r)

            num *= 2
            if num >= 1:
                num -= 1
                _r.append("1")
            else:
                _r.append("0")
        return "ERROR"
