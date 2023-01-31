class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        return sum([
            words1.count(i) == words2.count(i) == 1
            for i in (set(words1) & set(words2))
        ])
