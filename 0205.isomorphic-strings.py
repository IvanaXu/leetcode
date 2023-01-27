class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = set()
        for _s, _t in zip(s, t):
            st.add(_s+_t)
        return len(set(s)) == len(set(t)) == len(set(st))
