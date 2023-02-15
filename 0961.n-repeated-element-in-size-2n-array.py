class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        _r, _l = {}, len(nums)
        for i in nums:
            _n = _r.get(i, 0)
            _n += 1
            _r[i] = _n
            
            if _n >= _l//2:
                return i
