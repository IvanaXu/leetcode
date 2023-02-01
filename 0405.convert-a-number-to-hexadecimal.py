N = int("ffffffff", 16)
class Solution:
    def toHex(self, num: int) -> str:
        return f"{num + (0 if num >= 0 else N+1):x}"
