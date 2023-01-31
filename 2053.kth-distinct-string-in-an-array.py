class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        _r1, _r2 = [], set()
        for a in arr:
            if a not in _r1:
               _r1.append(a)
            else:
                _r2.add(a)
        return ([i for i in _r1 if i not in _r2] + [""]*k)[k-1]
