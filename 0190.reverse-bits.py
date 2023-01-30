class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{n:32b}".replace(" ", "0")[::-1], 2)
