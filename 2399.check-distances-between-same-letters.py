c = "abcdefghijklmnopqrstuvwxyz"
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        _c, _r = set(), [-1 for i in c]
        for n, v in enumerate(s):
            k = c.index(v)
            _c.add(v)

            if _r[k] == -1:
                _r[k] = n
            else:
                _r[k] = n-_r[k]-1
        
        for v in _c:
            k = c.index(v)
            if _r[k] != distance[k]:
                return False
        return True
