class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # return max([-1] + [
        #     v2-v1
        #     for n1, v1 in enumerate(nums)
        #     for n2, v2 in enumerate(nums)
        #     if n1 < n2 and v1 < v2
        # ])
        _max, _last = -1, nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < _last:
                cal = _last - nums[i]
                if cal > _max:
                    _max = cal
            elif nums[i] > _last:
                _last = nums[i]
        return _max
