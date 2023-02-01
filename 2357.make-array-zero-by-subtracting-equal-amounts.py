class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = 0
        while True:
            if sum(nums) == 0:
                break
            
            _min = min([i for i in nums if i > 0])
            nums = [i-_min if i > 0 else 0 for i in nums]
            n += 1
        return n
