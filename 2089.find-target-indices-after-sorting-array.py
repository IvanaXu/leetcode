class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [n for n, v in enumerate(sorted(nums)) if v == target]
