class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        _maxc, _minp = 0, prices[0]
        for p in prices[1:]:
            if p < _minp:
                _minp = p
            
            c = p - _minp
            if c > _maxc:
                _maxc = c
        return _maxc
