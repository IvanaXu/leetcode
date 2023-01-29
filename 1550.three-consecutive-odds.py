class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return "111" in "".join([str(i) for i in map(lambda x: x%2, arr)])
