class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([stones.count(i) for i in jewels])
