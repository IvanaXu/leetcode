class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = {
            "1": "Gold Medal",
            "2": "Silver Medal",
            "3": "Bronze Medal",
        }
        _score = {
            v: rank.get(str(n+1), str(n+1))
            for n, v in enumerate(sorted(set(score), reverse=True))
        }
        return [_score[v] for v in score]
