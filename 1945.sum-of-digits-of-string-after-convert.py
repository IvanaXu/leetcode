c = {
    _v: str(_n+1)
    for _n, _v in enumerate("abcdefghijklmnopqrstuvwxyz")
}
sget = lambda x: sum([int(i) for i in str(x)])
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        _r = "".join([c.get(i) for i in s])
        for _ in range(k):
            _r = sget(_r)
        return _r
