class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        _r = [-1, -1]
        for n, v in enumerate(nums):
            if v == target:
                _r = [n if _r[0] == -1 else _r[0], n]
            elif v > target:
                break
        return _r
