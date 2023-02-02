class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # a ^ b = c then c ^ b = a
        
        _r = [first]
        for n, e in enumerate(encoded):
            _r.append(_r[n] ^ e)
        return _r
