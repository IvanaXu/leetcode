class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        _r, _l = set(), len(digits)
        for n1 in range(_l):
            for n2 in range(_l):
                for n3 in range(_l):
                    if digits[n1] != 0 and n1 != n2 and n2 != n3 and n3 != n1:
                        c = digits[n1]*100 + digits[n2]*10 + digits[n3]
                        if c%2 == 0:
                            _r.add(c)
        return sorted(_r)
