class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 左右累乘
        _l = len(nums)
        r, _left, _right = [1 for n in range(_l)], 1, 1
        for n in range(_l):
            r[n] *= _left
            _left *= nums[n]

            r[-(n+1)] *= _right
            _right *= nums[-(n+1)]
        return r
