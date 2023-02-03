class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum([
            guess[0] == answer[0],
            guess[1] == answer[1],
            guess[2] == answer[2],
        ])
