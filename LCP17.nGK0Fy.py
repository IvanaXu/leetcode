class Solution:
    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for i in s:
            if i == "A":
                x = 2 * x + y
            elif i == "B":
                y = 2 * y + x
        return x + y
