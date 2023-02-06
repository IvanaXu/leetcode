class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        _r = {}
        for i in items1:
            if i[0] not in _r:
                _r[i[0]] = i[1]
        for i in items2:
            if i[0] not in _r:
                _r[i[0]] = i[1]
            else:
                _r[i[0]] += i[1]
        return [
            [_k, _r[_k]]
            for _k in sorted(_r.keys())
        ]
