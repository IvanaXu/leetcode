class Solution:
    def isNumber(self, s: str) -> bool:
        _r = {
            "e": "", # 2.718281828459045
            "inf": "",
            "-inf": "",
            "+inf": "",
            "Infinity": "",
            "-Infinity": "",
            "+Infinity": "",
        }
        try:
            float(_r.get(s, s))
            return True
        except:
            return False
