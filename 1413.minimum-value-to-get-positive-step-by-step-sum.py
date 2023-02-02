class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        _l, startValue = len(nums), 1
        while True:
            _k, _n = True, startValue
            for n, v in enumerate(nums):
                _n += v

                if _n < 1:
                    _k = False
                    startValue += 1
                    break
            
            if _k:
                return startValue
