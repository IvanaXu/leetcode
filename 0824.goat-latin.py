class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        _r = []
        for n, s in enumerate(sentence.split(" ")):
            _s = ""
            for c in "AEIOUaeiou/":
                if s.startswith(c):
                    _s = f"{s}ma{'a'*(n+1)}"
                    break
            if c == "/":
                _s = f"{s[1:]}{s[0]}ma{'a'*(n+1)}"
            _r.append(_s)
        return " ".join(_r)
