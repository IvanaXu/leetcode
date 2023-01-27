class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import datetime
        DT = {
            0: "Monday", 
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday",
        }
        return DT.get(datetime.datetime(year=year, month=month, day=day).timetuple().tm_wday, 0)
