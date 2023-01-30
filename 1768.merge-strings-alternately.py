class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        _r, _l1, _l2 = "", len(word1), len(word2)
        for n in range(max([_l1, _l2])):
            _r += f"{'' if n >= _l1 else word1[n]}{'' if n >= _l2 else word2[n]}"
        return _r
