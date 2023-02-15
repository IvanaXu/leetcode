class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        _r1, _rm = set(), set()
        for i in nums:
            if i not in _r1:
                _r1.add(i)
            else:
                _rm.add(i)
        return list(_r1-_rm)[0]
