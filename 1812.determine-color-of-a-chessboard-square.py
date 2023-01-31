class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        c1, c2 = coordinates[0], coordinates[1]
        if c1 in "aceg":
            return int(c2)%2 == 0
        else:
            return int(c2)%2 == 1
