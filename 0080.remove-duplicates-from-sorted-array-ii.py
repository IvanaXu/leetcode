class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        _n, _v, _l = 0, 99999, len(nums)
        for i in range(_l-1, -1, -1):
            v = nums[i]
            if _v != v:
                _v = v
                _n = 1
            elif _v == v:
                if _n == 1:
                    _n += 1
                else:
                    nums.pop(i)
        return len(nums)
