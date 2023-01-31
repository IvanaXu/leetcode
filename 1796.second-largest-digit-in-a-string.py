c = "1234567890"
class Solution:
    def secondHighest(self, s: str) -> int:
        _1, _2 = -1, -1
        for i in s:
            if i in c:
                i = int(i)
                
                if i > _1:
                    _2 = _1
                    _1 = i
                elif i != _1 and i > _2:
                    _2 = i
        return _2
