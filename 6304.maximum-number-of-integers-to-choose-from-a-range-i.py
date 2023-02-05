class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        _r, banned = 0, set(banned)
        for n in range(1, n+1):
            if n not in banned:
                if maxSum == 0:
                    break
                
                if n <= maxSum:
                    _r += 1
                    maxSum -= n
        return _r
