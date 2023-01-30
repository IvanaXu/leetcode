class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            [_3, _2, _1] = sorted(nums[:3])
            for i in nums[3:]:
                if i > _1:
                    _3 = _2
                    _2 = _1
                    _1 = i
                elif i > _2:
                    _3 = _2
                    _2 = i
                elif i > _3:
                    _3 = i
            return _3
