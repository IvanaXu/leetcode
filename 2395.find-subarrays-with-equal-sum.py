class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        _r, _l = [], len(nums)
        for n in range(_l-1):
            v1, v2 = nums[n], nums[n+1]
            _s = v1 + v2
            if _s not in _r:
                _r.append(_s)
            else:
                return True
        return False
