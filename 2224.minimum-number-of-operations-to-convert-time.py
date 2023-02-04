# Python2
class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        T1, T2, T3, T4 = 60, 15, 5, 1
        _r = 0

        from datetime import datetime
        _f = "%Y-%m-%d %H:%M:%S"
        mins = (
            datetime.strptime("2000-01-01 {0}:00".format(correct), _f) 
            - 
            datetime.strptime("2000-01-01 {0}:00".format(current), _f)
        ).seconds//60

        while True:
            if mins >= T1:
                _r += mins//T1
                mins = mins%T1
            elif mins >= T2:
                _r += mins//T2
                mins = mins%T2
            elif mins >= T3:
                _r += mins//T3
                mins = mins%T3
            elif mins >= T4:
                _r += mins//T4
                mins = mins%T4
            elif mins == 0:
                return _r

# Python3
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        T1, T2, T3, T4 = 60, 15, 5, 1
        _r = 0
        from datetime import datetime
        mins = (
            datetime.fromisoformat(f"2000-01-01 {correct}:00") 
            - 
            datetime.fromisoformat(f"2000-01-01 {current}:00")
        ).seconds//60

        while True:
            if mins >= T1:
                _r += mins//T1
                mins = mins%T1
            elif mins >= T2:
                _r += mins//T2
                mins = mins%T2
            elif mins >= T3:
                _r += mins//T3
                mins = mins%T3
            elif mins >= T4:
                _r += mins//T4
                mins = mins%T4
            elif mins == 0:
                return _r
