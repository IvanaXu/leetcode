class Solution:
    def search(self, nums: List[int], target: int) -> int:
        _r = 0
        for v in nums:
            if v == target:
                _r += 1
            elif v > target:
                break
        return _r
