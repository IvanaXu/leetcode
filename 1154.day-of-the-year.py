class Solution:
    def dayOfYear(self, date: str) -> int:
        import datetime
        return datetime.date.fromisoformat(date).timetuple().tm_yday
