class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        import datetime
        _r = (
            datetime.date.fromisoformat(date1) - 
            datetime.date.fromisoformat(date2)
            ).days
        return abs(_r)
