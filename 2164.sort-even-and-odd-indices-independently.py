class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        _r0, _r1 = [], []
        for n, v in enumerate(nums):
            if n%2 == 0:
                _r0.append(v)
            else:
                _r1.append(v)
        # 
        nums[0::2] = sorted(_r0)
        nums[1::2] = sorted(_r1, reverse=True)
        return nums
