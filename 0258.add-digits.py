class Solution:
    def addDigits(self, num: int) -> int:
        get = lambda x: sum([int(i) for i in str(x)])
        while True:
            num = get(num)
            if num//10 == 0:
                return num
