class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while True:
            if original in nums:
                original = original * 2
            else:
                return original
