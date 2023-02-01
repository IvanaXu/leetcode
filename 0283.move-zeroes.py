class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        e = -1
        for n, v in enumerate(nums):
            if v == 0:
                nums.remove(v)
                nums.append(v)
        return nums
