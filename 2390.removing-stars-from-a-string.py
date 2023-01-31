class Solution:
    def removeStars(self, s: str) -> str:
        if len(s) == s.count("*")*2:
            return ""
        
        _r = []
        for i in s:
            if i == "*":
                # Back
                _r.pop() 
            else:
                _r.append(i)
        return "".join(_r)
