class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(i) for n in nums for i in str(n)]
