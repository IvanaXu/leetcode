class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        """
        [1, 4]
        1 ^ 0 ^ 1 ^ 4 ^ 1 ^ 4 ^ 0 ^ 4 = 1^ 4 = 5
        """
        return reduce(lambda x, y: x^y, nums)
