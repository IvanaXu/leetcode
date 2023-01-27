class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        _c, max_n, max_v = {}, 0, nums[0]
        for i in nums:
            if i not in _c:
                _c[i] = 1
            else:
                _c[i] += 1

                _n = _c[i]
                if _n > max_n:
                    max_n = _n
                    max_v = i
        return max_v
