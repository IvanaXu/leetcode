class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        _l, _r, _lk = len(questions)//2, {}, []
        for q in questions:
            _r[q] = 1 if q not in _r else _r[q]+1
        for _v, _k in sorted(
            [(_v, _k) for _k, _v in _r.items()], reverse=True):
            _l = _l - _v
            _lk.append(_k)

            if _l <= 0:
                break
        return len(_lk)
