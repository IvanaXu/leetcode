class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        _r, _s = [], set(nums)
        
        for n in range(len(nums)):
            if n+1 not in _s:
                _r.append(n+1)
        return _r

