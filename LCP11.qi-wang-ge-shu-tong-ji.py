class Solution:
    def expectNumber(self, scores: List[int]) -> int:
        # [1, 1] = 1/2+1/2 = 1
        # [1, 2] = 1 + 1 = 2
        # [1, 1, 2] = 1/2+1/2+1 = 2
        return len(set(scores))
