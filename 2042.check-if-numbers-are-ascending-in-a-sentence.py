class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        _r = [
            int(i) for i in s.split(" ")
            if (
                i.startswith("1") or
                i.startswith("2") or
                i.startswith("3") or
                i.startswith("4") or
                i.startswith("5") or
                i.startswith("6") or
                i.startswith("7") or
                i.startswith("8") or
                i.startswith("9")
            )
        ]
        return _r == sorted(set(_r))
