class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        _max = 0
        for n, v in enumerate(number):
            if v == digit:
                _number = list(number)
                _number.pop(n)
                _number = int("".join(_number))
                if _number > _max:
                    _max = _number
        return str(_max)
