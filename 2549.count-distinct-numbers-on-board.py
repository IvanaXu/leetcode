class Solution:
    def distinctIntegers(self, n: int) -> int:
        _r = set([n])

        while True:
            _lr = _r.copy()
            for x in _lr:
                for i in range(1, n+1):
                    if x%i == 1:
                        _r.add(i)

            if len(_lr) == len(_r):
                return len(_r)
