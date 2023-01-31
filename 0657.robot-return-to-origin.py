class Solution:
    def judgeCircle(self, moves: str) -> bool:
        point = {"x": 0, "y": 0}
        for m in moves:
            if m == "R":
                point["x"] += 1
            elif m == "L":
                point["x"] -= 1
            elif m == "U":
                point["y"] += 1
            elif m == "D":
                point["y"] -= 1
        return point["x"] == 0 and point["y"] == 0
