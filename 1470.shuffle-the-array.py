class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        _r, _l = [], len(nums)
        for _x, _y in zip(nums[:_l//2], nums[_l//2:]):
            _r.extend([_x, _y])
        return _r
