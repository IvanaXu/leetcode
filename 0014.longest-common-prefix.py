class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l, m, mk = "", 0, ""
        for i in strs:
            j = len(i)
            if m == 0 or j <= m:
                m = j
                l = i
        for k in range(0, m):
            mk = l[:m-k]
            r = set()
            for i in strs:
                r.add(i[:m-k])
            if len(r) == 1:
                break
            mk = ""
        return mk
