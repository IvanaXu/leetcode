class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # _allowed = set(allowed)
        # return sum([set(i)|_allowed == _allowed for i in words])
        return sum([
            min([i in allowed for i in w])
            for w in words
        ])
