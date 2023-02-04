class Solution:
    def countElements(self, nums: List[int]) -> int:
        # 非最大 非最小
        _min, _max = 999999, -999999
        for n in nums:
            if n > _max:
                _max = n
            if n < _min:
                _min = n
        return len([n for n in nums if n not in [_min, _max]])
