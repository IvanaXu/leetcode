C1 = 10000
C2 = 1000000000
C3 = 100
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        _b, _h = "", ""
        if length >= C1 or width >= C1 or height >= C1 or (length*width*height) >= C2:
            _b = "Bulky"
        if mass >= C3:
            _h = "Heavy"
        
        if _b == "Bulky" and _h == "Heavy":
            return "Both"
        elif _b != "Bulky" and _h != "Heavy":
            return "Neither"
        else:
            return _b + _h
