class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for l in letters:
            if ord(l) > ord(target):
                return l
        return letters[0]
