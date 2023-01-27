class Solution:
    def maximum69Number (self, num: int) -> int:
        _ret = list(str(num))

        for n, i in enumerate(_ret):
            if i == "6":
                _ret[n] = "9"
                break

        return int("".join(_ret))
