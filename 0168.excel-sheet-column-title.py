class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # YY, 675=25+26*25
        # YYY, 17575=25+26*25+26*26*25
        # n - 1
        n, _r = columnNumber, ""
        while n:
            n -= 1
            _r = chr(n%26 + 65) + _r
            n //= 26
        return _r
