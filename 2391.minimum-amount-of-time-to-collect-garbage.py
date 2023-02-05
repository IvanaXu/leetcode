class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        _travel, _v = [0], 0
        for v in travel:
            _v += v
            _travel.append(_v)

        _driver = {i:0 for i in "MPG"}
        _cleanr = {i:0 for i in "MPG"}
        for _n, _g in enumerate(garbage):
            for _ig in _g:
                _cleanr[_ig] += 1
                _driver[_ig] = _travel[_n]
        return sum(_driver.values()) + sum(_cleanr.values())
