class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        _r, _l = set(), []
        for n1 in range(1, n+1):
            for n2 in range(1, n+1):
                if n2 > n1:
                    caln = eval(f"{n1}/{n2}")
                    
                    if caln not in _r:
                        _r.add(caln)
                        _l.append(f"{n1}/{n2}")
        return _l
