class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        _r, _l = {}, len(nums)
        if _l == 1:
            return nums[0]
        
        for i in nums:
            if i not in _r:
                _r[i] = 1
            else:
                _r[i] += 1

                if _r[i] * 2 > _l:
                    return i
        return -1
