class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        _r0, _r1 = [], []
        for i in nums:
            if i%2 == 0:
                _r0.append(i)
            else:
                _r1.append(i)
        return _r0 + _r1
