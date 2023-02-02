class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        _r = {}
        for ir in ranks:
            _r[ir] = 1 if ir not in _r else _r[ir]+1
        
        _k, _maxv = _r.keys(), max(_r.values())
        if len(set(suits)) == 1:
            return "Flush"
        elif _maxv >= 3:
            return "Three of a Kind"
        elif _maxv == 2:
            return "Pair"
        elif len(_k) == 5:
            return "High Card"
