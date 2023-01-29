class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        _r = set()
        while nums:
            _min, _max = min(nums), max(nums)
            _r.add((_min + _max)/2)
            nums.remove(_min)
            nums.remove(_max)
        return len(_r)
