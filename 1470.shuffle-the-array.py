class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        _r, _lh = [], len(nums)//2
        for _x, _y in zip(nums[:_lh], nums[_lh:]):
            _r.extend([_x, _y])
        return _r
