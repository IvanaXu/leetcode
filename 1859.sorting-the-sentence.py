class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join(
            [
                i[:-1]
                for i in sorted(s.split(" "), key=lambda x: x[-1])
            ]
        )
