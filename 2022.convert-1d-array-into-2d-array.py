class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        _l = len(original)
        if m * n != _l:
            return []
        else:
            return [
                original[i*n: (i+1)*n]
                for i in range(m)
            ]
