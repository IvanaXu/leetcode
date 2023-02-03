# Python2
def match(a, b):
    if a == b:
        return "平稳"
    elif a > b:
        return "下降"
    elif a < b:
        return "上升"
    else:
        return ""

class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:    
        _d, _maxd, n = 0, 0, len(temperatureA)
        for _n in range(0, n):
            if _n > 0:
                if match(_stA, temperatureA[_n]) == match(_stB, temperatureB[_n]):
                    _d += 1
                    if _d > _maxd:
                        _maxd = _d
                else:
                    _d = 0
            _stA, _stB = temperatur
# Python3
