class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f"{n:_}".replace("_", ".")
