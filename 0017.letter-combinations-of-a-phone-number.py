class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        r, n = [], 0
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        for i in digits:
            n += 1
            d = dic[i]
            if n == 1:
                for j in d:
                    r.append(j)
            else:
                r1 = []
                for j in d:
                    for k in r:
                        r1.append(k+j)
                r = r1
        return r
