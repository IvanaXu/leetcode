class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mpath, _r = "", {}
        for p in paths:
            for np, ip in enumerate(p.split(" ")):
                if np == 0:
                    mpath = ip
                else:
                    [file, content] = ip.split("(")

                    if content not in _r:
                        _r[content] = [f"{mpath}/{file}"]
                    else:
                        _r[content].append(f"{mpath}/{file}")
        return [v for v in _r.values() if len(v) > 1]
