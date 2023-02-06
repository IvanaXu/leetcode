class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        _r, _k, _max, _arr = 0, 0, max(arr), set(arr)
        for n in range(1, _max+k+1):
            if n not in _arr:
                _k += 1
                _r += n
            if _k == k:
                return n
