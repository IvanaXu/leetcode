class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(map(lambda x: len(f"{x}")%2 == 0, nums))
