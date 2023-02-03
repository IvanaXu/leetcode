class Solution:
    def minCount(self, coins: List[int]) -> int:
        _t = {
            1: 1,
            2: 1,
            3: 2,
            4: 2,
            5: 3,
            6: 3,
            7: 4,
            8: 4,
            9: 5,
            10: 5,
        }
        return sum([_t.get(c) for c in coins])
