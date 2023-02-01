# Python
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        _half = int(area ** 0.5)
        for _l in range(_half, area+1):
            _w = area//_l
            if _l * _w == area:
                if _w > _l:
                    _l, _w = _w, _l
                return [_l, _w]

# Python3
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        _half = int(area ** 0.5)
        for _l in range(_half, area+1):
            _w = area//_l
            if _l * _w == area:
                if _w > _l:
                    _l, _w = _w, _l
                return [_l, _w]

