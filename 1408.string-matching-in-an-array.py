class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [
            i for i in set([
                w1 if w1 in w2 else (w2 if w2 in w1 else "")
                for w1 in words
                for w2 in words
                if w1 != w2
            ]) if i
        ]
