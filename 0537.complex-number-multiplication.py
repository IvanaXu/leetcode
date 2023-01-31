class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        _r = eval(f"({num1.replace('i','J')}) * ({num2.replace('i','J')})")
        return f"{int(_r.real)}+{int(_r.imag)}i"
