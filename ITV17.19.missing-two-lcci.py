#
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        _r, _n, _l = [], 0, len(nums)
        for i in range(1, _l+2+1):
            if i in nums:
                nums.remove(i)
            else:
                _n += 1
                _r.append(i)
            if _n == 2:
                return _r

#
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        _nums = set(nums)
        _r, _n, _l = [], 0, len(_nums)
        for i in range(1, _l+2+1):
            if i in _nums:
                _nums.remove(i)
            else:
                _n += 1
                _r.append(i)
            if _n == 2:
                return _r
