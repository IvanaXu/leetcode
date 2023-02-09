class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _r = {}
        for s in strs:
            _k = "".join(sorted(s))
            if _k not in _r:
                _r[_k] = [s]
            else:
                _r[_k].append(s)
        return list(_r.values())
