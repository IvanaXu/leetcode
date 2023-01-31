class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        _r1, _r2 = set(), set()
        for i in nums:
            if i not in _r1:
                _r1.add(i)
            else:
                _r2.add(i)
        return list(_r1 - _r2)
