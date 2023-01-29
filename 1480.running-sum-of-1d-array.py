class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        _r, _s = [], 0
        for i in nums:
            _s += i
            _r.append(_s)
        return _r            
