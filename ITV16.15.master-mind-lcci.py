class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        # 只猜对颜色但槽位猜错了 > 猜对颜色次数 - match
        # print(collections.Counter(solution) & collections.Counter(guess))
        C = "RYGB"
        _cs = {c: 0 for c in C}
        _cg = {c: 0 for c in C}
        _1, _2 = 0, 0

        for _s, _g in zip(solution, guess):
            if _s == _g:
                _1 += 1
            _cs[_s] += 1
            _cg[_g] += 1
        _2 = sum([min([_cs[c], _cg[c]]) for c in C])
        return [_1, _2-_1]
