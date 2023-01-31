class Solution:
    def similarPairs(self, words: List[str]) -> int:
        return len([
            (v1, v2)
            for n1, v1 in enumerate(words)
            for n2, v2 in enumerate(words)
            if n1 > n2 and set(v1) == set(v2)
        ])
