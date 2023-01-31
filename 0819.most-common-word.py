class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        _r = {}
        for i in paragraph.lower().replace(",", " ").split(" "):
            if i:
                i = i.replace(".","")
                i = i.replace(";","")
                # i = i.replace(",","")
                i = i.replace("'","")
                i = i.replace("?","")
                i = i.replace("!","")

                if i not in banned:
                    if i not in _r:
                        _r[i] = 1
                    else:
                        _r[i] += 1
        _max = max(_r.values())
        return [_k for _k, _v in _r.items() if _v == _max][0]
