# https://leetcode.cn/problems/two-sum/submissions/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = 0
        for i in nums:
            t = target - i
            if t in nums[n+1:]:
                return [n, nums[n+1:].index(t)+n+1]
            n += 1
