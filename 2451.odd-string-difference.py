# Python2
class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        c = {v: n for n, v in enumerate("abcdefghijklmnopqrstuvwxyz")}

        r = {}
        for w in words:
            _v, _r = "", ""
            for n, v in enumerate(w):
                if n == 0:
                    _v = v
                else:
                    _r += "/" + str(c.get(v,0) - c.get(_v,0))
                    _v = v
            # 
            if _r not in r:
                r[_r] = {"word": w, "cnts": 1}
            else:
                r[_r]["cnts"] += 1
        return [_v["word"] for _k, _v in r.items() if _v["cnts"] == 1][0]

# Python3
c = {v: n for n, v in enumerate("abcdefghijklmnopqrstuvwxyz")}
class Solution:
    def oddString(self, words: List[str]) -> str:
        r = {}
        for w in words:
            _v, _r = "", ""
            for n, v in enumerate(w):
                if n == 0:
                    _v = v
                else:
                    _r += f"/{c.get(v,0) - c.get(_v,0)}"
                    _v = v
            # 
            if _r not in r:
                r[_r] = {"word": w, "cnts": 1}
            else:
                r[_r]["cnts"] += 1
        return [_v["word"] for _k, _v in r.items() if _v["cnts"] == 1][0]
