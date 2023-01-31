class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        _r = {}
        for i in nums:
            if i not in _r:
                _r[i] = 1
            else:
                _r[i] += 1
        return sorted(nums, key=lambda x: (_r[x], -x))
