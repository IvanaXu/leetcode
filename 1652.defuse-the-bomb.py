class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        _l, _code = len(code), code*3
        return [
            sum(_code[n+1: n+k+1]) if k > 0 else (
                sum(_code[n+k: n]) if k < 0 else 0
            )
            for n in range(0+_l, _l+_l)
        ]
