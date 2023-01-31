class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        c1 = set("qwertyuiop")
        c2 = set("asdfghjkl")
        c3 = set("zxcvbnm")

        _r = []
        for w in words:
            _w = set(w.lower())
            if c1.issuperset(_w) or c2.issuperset(_w) or c3.issuperset(_w):
                _r.append(w)
        return _r
