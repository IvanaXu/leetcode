class Solution:
    def romanToInt(self, s: str) -> int:
        _r = 0
        while s:
            if s.startswith("M"):
                s = s[1:]
                _r += 1000
            elif s.startswith("D"):
                s = s[1:]
                _r += 500
            # 
            elif s.startswith("CD"):
                s = s[2:]
                _r += 400
            elif s.startswith("CM"):
                s = s[2:]
                _r += 900
            elif s.startswith("C"):
                s = s[1:]
                _r += 100
            #
            elif s.startswith("L"):
                s = s[1:]
                _r += 50
            # 
            elif s.startswith("XL"):
                s = s[2:]
                _r += 40
            elif s.startswith("XC"):
                s = s[2:]
                _r += 90
            elif s.startswith("X"):
                s = s[1:]
                _r += 10
            # 
            elif s.startswith("V"):
                s = s[1:]
                _r += 5
            # 
            elif s.startswith("IV"):
                s = s[2:]
                _r += 4
            elif s.startswith("IX"):
                s = s[2:]
                _r += 9
            elif s.startswith("III"):
                s = s[3:]
                _r += 3
            elif s.startswith("II"):
                s = s[2:]
                _r += 2
            elif s.startswith("I"):
                s = s[1:]
                _r += 1
        return _r
