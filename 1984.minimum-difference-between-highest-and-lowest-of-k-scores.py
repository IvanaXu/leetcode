class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        _min, _nums = 999999, sorted(nums, reverse=True)

        for i in range(len(_nums)-k+1):
            j = _nums[i: i+k]
            _min = min(_min, max(j) - min(j))
        return 0 if _min == 999999 else _min
