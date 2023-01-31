c = {v:n for n, v in enumerate("abcdefghijklmnopqrstuvwxyz")}

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        _1 = "".join([str(c.get(i)) for i in firstWord])
        _2 = "".join([str(c.get(i)) for i in secondWord])
        _3 = "".join([str(c.get(i)) for i in targetWord])
        return (int(_1) + int(_2)) == int(_3)
