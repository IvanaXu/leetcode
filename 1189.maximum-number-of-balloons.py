class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        _r = {}
        for t in text:
            _r[t] = 1 if t not in _r else _r[t]+1
        
        return min([
            _r.get("b", 0)//1, 
            _r.get("a", 0)//1, 
            _r.get("l", 0)//2, 
            _r.get("o", 0)//2, 
            _r.get("n", 0)//1,
        ])
